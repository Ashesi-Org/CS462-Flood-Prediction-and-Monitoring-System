from http.server import BaseHTTPRequestHandler, HTTPServer

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"user_action_count{action=\"login\"} 5\n")
            self.wfile.write(b"user_action_count{action=\"logout\"} 2\n")

server = HTTPServer(('localhost', 9091), MetricsHandler)
print("Serving metrics on http://localhost:9091/metrics")
server.serve_forever()
