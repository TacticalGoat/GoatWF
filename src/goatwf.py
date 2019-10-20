from werkzeug.wrappers import Request, Response
from .default_responses import response404

class GoatWF(object):
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        return self.handle_request(environ, start_response)
    
    def handle_request(self, environ, start_response):
        request = Request(environ)
        response = None
        for path, view in self.routes.items():
            if path == request.path:
                response = view(environ, start_response)
        if response is None:
            return response404(environ, start_response)
        return response

    def route(self, path):
        def inner(view):
            self.routes[path] = view
            return view
        return inner    