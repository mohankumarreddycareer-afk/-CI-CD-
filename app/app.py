import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {"status": "healthy"}
        else:
            response = {
                "message": "Welcome to CI-CD-Project",
                "status": "running"
            }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 5000), AppHandler)
    print("CI-CD-Project running on http://127.0.0.1:5000")
    server.serve_forever()
