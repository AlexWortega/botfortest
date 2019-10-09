from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
import pywaves


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        #if(self.):

        self.wfile.write(b'everything okay ')
        self.wfile.write(str.encode(self.path))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'transkation component')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('', 8087), SimpleHTTPRequestHandler)
httpd.serve_forever()