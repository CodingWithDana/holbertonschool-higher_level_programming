from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class simpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # check the requested PATH
        if self.path == '/':
            # basic text response
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # JSON response
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data)

        elif self.path == '/status':
            # status endpoint
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # undefined endpoint
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

# start the server on port 8000
def run(server_class=HTTPServer, handler_class=simpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
