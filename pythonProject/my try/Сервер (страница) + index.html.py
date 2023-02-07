from http.server import HTTPServer, CGIHTTPRequestHandler
server_data = ('localhost', 6878)
server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()