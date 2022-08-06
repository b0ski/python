from http.server import BaseHTTPRequestHandler
from routes.main import routes
from pathlib import Path
import simplejson


class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        status = 200

        if self.path in routes:
            print(routes[self.path])
            route_content = routes[self.path]['template']
            filepath = Path("templates/{}".format(route_content))
            if filepath.is_file():
                content_type = "text/html"
                response_content = open("templates/{}".format(route_content))
                response_content = response_content.read()

            else:
                content_type = "text/plain"
                response_content = "404 Not Found"

        else:
            content_type = "text/plain"
            response_content = "404 Not Found"

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(bytes(response_content, "UTF-8"))

    def do_POST(self):
        if self.path == '/json':
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            self.send_response(200)
            self.end_headers()
            data = simplejson.loads(self.data_string)
            print(data)
            self.send_response(200)
            self.send_header('Content-type',"text/html")
            self.end_headers()
            response_content = "ok"
            self.wfile.write(bytes(response_content, "UTF-8"))
