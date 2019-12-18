import http.server
import socketserver
import requests
import json

def some_function():
    print("some_function got called")
    filename = "../database/JSON.json"
    with open(filename, 'r') as f:
        datastore = json.load(f)
        if datastore:
            #add recipe
            with open(filename, 'w') as f:
                json.dump(datastore, f)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/add_recipe':
            # Insert your code here
            some_function()
            self.path = '/index.html' #changing path to go to the main web site
        super().do_GET() #using base function of http.server.SimpleHTTPRequestHandler to load page

        self.send_response(200)

PORT = 8080

def start_server():

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
