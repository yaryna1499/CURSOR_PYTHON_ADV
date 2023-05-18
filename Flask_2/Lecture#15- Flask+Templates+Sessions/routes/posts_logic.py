from app import app, db
from flask import render_template, request, redirect, session
from models import User, Post



@app.route("/create_post")
def create_post():
    try:
        if session["user"]:
            return render_template("post.html")
    except KeyError:
        return "Please, sign in!"  ##to show this message into template
    


@app.route("/edit_post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    # post = db.session.query(Post).filter_by(post_id=post_id)
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':

        post.edit_post(
        new_header = request.form['post_header'],
        new_text = request.form['post_text']
        )
        return redirect("/")

    return render_template("edit_post.html", post=post)
    



@app.route("/save_post", methods=['POST'])
def save_post():
    data = request.form
    post = Post(
        user_id = session["user"]['id'],
        post_header = data.get("post_header"),
        post_text = data.get("post_text")
    )
    db.session.add(post)
    db.session.commit()
    session["post"] = post.serialize
    return redirect("/")