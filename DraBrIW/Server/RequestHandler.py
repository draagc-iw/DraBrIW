from http.server import BaseHTTPRequestHandler
import json
from .handlers import user_post, user_get, user_put, drinks_get, drinks_post



class RequestHandler(BaseHTTPRequestHandler):
    get_paths = {
        '/users': lambda: user_get(),
        '/drinks': lambda: drinks_get(),
    }

    put_paths = {
        '/users': lambda body: user_put(body)
    }

    post_paths = {
        '/users': lambda body: user_post(body),
        '/drinks': lambda body: drinks_post(body)
    }

    def do_GET(self):
        path = self.path
        res, code = RequestHandler.get_paths[path]() if path in RequestHandler.get_paths.keys() else (None, 404)
        self._respond(res, code)

    def do_PUT(self):
        body = self._get_request_body()
        path = self.path
        res, code = RequestHandler.put_paths[path](body) if path in RequestHandler.put_paths.keys() else (None, 404)
        self._respond(res, code)

    def do_POST(self):
        body = self._get_request_body()
        path = self.path
        res, code = RequestHandler.post_paths[path](body) if path in RequestHandler.post_paths.keys() else (None, 404)
        self._respond(res, code)

    def _respond(self, response, code):
        if (response, code) != (None, 404):
            self._set_headers(code)
            self.wfile.write(response)
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": f"No such path {self.path}"}).encode('utf-8'))

    def _set_headers(self, code):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def _get_base_path(self):
        query_params_start = self.path.find("?")
        return self.path[:query_params_start]

    def _get_request_body(self):
        content_length = int(self.headers["Content-Length"])
        return self.rfile.read(content_length)


