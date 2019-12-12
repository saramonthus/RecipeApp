import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

def main():
    print ("Hello")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

if __name__ == '__main__':
    main()
