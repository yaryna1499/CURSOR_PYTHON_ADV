from flask import Flask, abort
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


@app.route("/datetime/", defaults={"zone": None})
@app.route("/datetime/<zone>")
def date_time_printer(zone):
    """
    This app returns date and time according to given timezone.
    The default is local server timezone (Europe/Kiev).
    Also available timezones:
    0: Greenwich,
    +2: GMT+2
    """
    app.logger.info(f"The chosen param is {zone}")
    params = {
        "0": "Etc/Greenwich",
        "+2": "Etc/GMT-2",
        None: "Europe/Kiev",
    }
    response_message = f"<h1>{datetime.now(tz=timezone(params[zone])).strftime('%Y-%m-%d %H:%M:%S %Z%z')}</h1>"
    if zone not in params:
        abort(406, "Timezone is wrong!")
    else:
        return response_message


@app.route("/datetime")
def date_time_doc():
    app.logger.info("Doc root was reached.")
    return date_time_printer.__doc__


if __name__ == "__main__":
    import logging

    app.logger.setLevel(logging.DEBUG)
    app.run("localhost", port=5000, debug=True)
