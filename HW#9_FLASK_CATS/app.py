import catday
import utils
from flask import *
import PIL.Image
import io
import logging
import random
from time import perf_counter
import os
import base64


app = Flask(__name__)



@app.route("/")
def hello_world():
    # TODO: use proper template instead of the following
    return render_template("index.html")


# Note:
#   If a rule ends with a slash and is requested without a slash by the user,
#   the user is automatically redirected to the same page with a trailing
#   slash attached.
#   If a rule does not end with a trailing slash and the user requests
#   the page with a trailing slash, a 404 not found is raised.
# So we try to always define rules with trailing slashes '/'


@app.route("/cats/")
def list_cats():
    msg = "There are {num} cats in our collection"
    return msg.format(num=len(catday.CATS))


def get_cat(numext, try_random=False):
    try:
        ret = catday.find_cat_file(numext=numext, try_random=try_random)
    except ValueError:  # integer unconvertable or wrong range
        abort(404, "Wrong image number")
    else:
        app.logger.debug('Retrieve image "%s" for ' 'base %s with ext "%s"', *ret)
        return ret


@app.route("/cats/cat<int:num>.<string:ext>")
def cat_original(num, ext):
    t_start = perf_counter()  # measure request time

    file, base, ext = get_cat(f"{num}.{ext}", try_random=False)

    name = f"cat{base}{ext}"  # the filename passed to browser

    app.logger.debug("Original extension is %s", file.suffix)

    # if the extension is different, perform conversion with PIL
    if ext.lower() != file.suffix.lower():
        try:
            img = PIL.Image.open(file)
            # Save to buffer in memory and serve with Flask
            buf = utils.ImageIO(img, ext=ext)
        except utils.ImageIOError as err:
            abort(400, str(err))
        else:
            # now our file gets mocked by conversion result
            file = buf

    # if the file has the same extension,
    # don't convert at all and return directly

    took = perf_counter() - t_start

    if app.logger.isEnabledFor(logging.DEBUG):
        msg = f"Request took {took * 1000:.2f} ms"
        app.logger.debug(msg)

    return send_file(file, as_attachment=False, download_name=name)


@app.route("/cats/catoftheday<name>")
def cat_modified(name):
    file, base, ext = get_cat(name, try_random=True)

    date = utils.DateTriple()  # try UADateTriple() here
    date_suffix = date.tostr(fmt="{day}_{month:.3}").lower()

    text = date.tostr(fmt="{weekday:.3},\n{day}\n{month:.3}")

    try:
        img = PIL.Image.open(file)
        bgcolor = (255, 255, 255, int(255 * 0.4))
        cut = catday.cutter.text_cutout(img, text, bgcolor=bgcolor)
        if ext in [".jpg", ".jpeg", ".jfif"]:
            # eliminate alpha-channel as JPEG has no alpha
            cut = cut.convert("RGB")
        file = utils.ImageIO(cut, ext=ext)
    except utils.ImageIOError as err:
        abort(400, str(err))

    # passed to browser
    name = f"catoftheday{base}-{date_suffix}{ext}"
    return send_file(file, as_attachment=False, download_name=name)



app.config['UPLOAD_FOLDER'] = 'static/images/user_uploads'

@app.route('/image_maker')
def image_maker():

    file_name = request.args.get("file_name")
    app.logger.debug(file_name)
    text = request.args.get("text")
    app.logger.debug("text caught: %s", text)

    message = "Image uploaded successfully! Enjoy the result!"


    file = PIL.Image.open(f"{app.config['UPLOAD_FOLDER']}/{file_name}")
    result_image = utils.textcut.cutter.text_cutout(file, text)
    result_image.save(os.path.join('static/images/user_result_images', file_name))

    return render_template("upload_page.html", message=message, image=file_name)



app.config['ALLOWED_EXTENSIONS'] = ['jpg', 'jpeg', "png", "gif"]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    app.logger.debug("method = %s", request.method)
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        

        file = request.files['file']
        input_text = request.form['user_text'].encode('utf-8')


        if file.filename == '' or not allowed_file(file.filename):
            return "No file choosen or unsupported format. Please try: .jpg/.jpeg/.png./gif"
        else:
            file.filename = file.filename.replace(" ", "")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            return redirect(url_for("image_maker", file_name=file.filename, text=input_text))
            

if __name__ == "__main__":
    import logging

    app.logger.setLevel(logging.DEBUG)
    app.run(host="127.0.0.1", port=5000, debug=True)
