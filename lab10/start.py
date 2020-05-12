from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8003)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
