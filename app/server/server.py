from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http import HTTPStatus
from app.classes.eshop.operations_module import basket
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/basket":
            self.send_response(200)
            self.send_header("Set-Cookie", "foo=bar")
            self.end_headers()
            self.wfile.write(bytes(basket.checkout().encode("utf-8")))


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


if __name__ == "__main__":
    run()
