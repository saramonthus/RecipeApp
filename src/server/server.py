import http.server
import socketserver
import requests
import json

# class raii(object):
#     """docstring for raii."""
#
#     def __init__(self):
#         print("construct")
#
#     def __enter__(self):
#         print("open")
#
#     def __exit__(self, value, type, traceback):
#         print("close")
#
# def raii_open():
#     return raii()
#
# with raii_open() as r:
#     print("inside with")

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
