from http.server import BaseHTTPRequestHandler
from routes.main import routes
from pathlib import Path
import json
from app.classes.eshop.operations_module import basket


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
        status = 200
        if self.path.endswith(".json"):
            content_type = "text/plain"
            self.send_response(status)
            self.send_header('Content-type', content_type)
            self.end_headers()

            raw_path = self.path
            raw_data = raw_path[1:]
            raw_data = raw_data[:-5]

            print(raw_data)

            raw_data = bytes('{"value_1": "ans_1", "value_2": "ans_2"}', "UTF-8")
            data = json.loads(raw_data)

            for item in data:
                print(data[item])

            response_content = "ok"
            self.wfile.write(bytes(response_content, "UTF-8"))
