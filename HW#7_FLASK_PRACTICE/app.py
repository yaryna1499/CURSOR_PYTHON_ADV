from functools import lru_cache
from flask import Flask, abort, request, Response
from statapi import methods
from additional.converter import to_bool


app = Flask(__name__)


@app.route("/stats/")
@lru_cache(maxsize=1)  # can use cuz no flask proxies refered
def stats_root():
    """List all methods."""
    ret = [mtd for mtd in methods]

    return f"<b>Available methods:</b><br>{repr(ret).strip('[]')}"


@app.route("/stats/<string:method>")
def stats(method):
    format = request.args.get("format")
    arguments = request.args.to_dict()

    for key, value in arguments.items():
        arguments[key] = to_bool(value)

    try:
        func = methods[method]
    except KeyError:
        abort(404, f"Method {method} not found")

    try:
        # format is set on a statapi module level defaults
        res, mime = func() if format is None else func(format=format)
    except Exception as exc:
        # TODO: add error reporting verbosity
        #       e.g. when format is not supported
        abort(400, f"Format {format} is not supported.")

    try:
        res, mime = func(**arguments)
    except TypeError:
        abort(400, "Incorrect arguments.")

    return Response(res, mimetype=mime)


if __name__ == "__main__":
    # We need to set logging to be able to see everything
    import logging

    app.logger.setLevel(logging.DEBUG)

    # (!) Never run your app on '0.0.0.0 unless you're deploying
    #     to production, in which case a proper WSGI application
    #     server and a reverse-proxy is needed
    #     0.0.0.0 means "run on all interfaces" -- insecure
    app.run(host="127.0.0.1", port=8000, debug=True)
