from .goatwf import GoatWF
from werkzeug.wrappers import Response

app = GoatWF()

@app.route("/home")
def home(environ, start_response):
    response = Response("Hello Homepage", mimetype="text/plain")
    return response(environ, start_response)


@app.route("/about")
def about(environ, start_response):
    response = Response("Hello About", mimetype="text/plain")
    return response(environ, start_response)