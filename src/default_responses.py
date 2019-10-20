from werkzeug import Response

def response404(environ, start_response):
    response = Response("Resource not found", mimetype="text/plain", status=404)
    return response(environ, start_response)