import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

def start_server():

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
