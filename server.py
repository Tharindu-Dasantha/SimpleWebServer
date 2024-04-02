from http.server import BaseHTTPRequestHandler, HTTPServer
import csv


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")
        

        # Open a CSV file and reads its content 
        with open('data.csv','r') as csvfile:
            content = csvfile.read()
            self.wfile.write(content.encode())


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
        server_address = ('', port)
        httpd  = server_class(server_address, handler_class)
        print(f"Server running on port {port}")
        httpd.serve_forever()


if __name__ == '__main__':
            run()




# return content in XML, JSON, CSV.  - DONE
# load HTML files and then serve content
# perform routing using HTTP Request Object

