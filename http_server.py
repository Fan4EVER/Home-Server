from http.server import HTTPServer, BaseHTTPRequestHandler

my_html = open("index.html", "r")

code = str(my_html.read())

HOST = "192.168.1.45"
PORT = 8000

class NeralHTTP(BaseHTTPRequestHandler):
	def do_GET(self):
	    self.send_response(200)
	    self.send_header("Content-Type", "text/html")
	    self.end_headers()
	    
	    
	    self.wfile.write(bytes(code, "utf-8"))
	    
server = HTTPServer((HOST, PORT), NeralHTTP)
print("Server now running on Host: " + HOST + " and Port " + str(PORT) + " ...")
server.serve_forever()
server.server_close()

