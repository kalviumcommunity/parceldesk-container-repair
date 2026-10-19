import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        body = b"ParcelDesk healthy\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    if os.environ.get("APP_MODE") != "production":
        raise SystemExit("ERROR: APP_MODE must be production")
    address = "127.0.0.1"
    server = HTTPServer((address, 8000), Handler)
    print(f"ParcelDesk listening on {address}:8000; APP_MODE=production", flush=True)
    server.serve_forever()
