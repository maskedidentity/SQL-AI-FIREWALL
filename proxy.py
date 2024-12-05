from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib import request, error
import socket

class SimpleHTTPProxy(SimpleHTTPRequestHandler):
    proxy_routes = {}
    
    @classmethod
    def set_routes(cls, proxy_routes):
        
        cls.proxy_routes = proxy_routes

    def do_GET(self):
        print(f"Full path: {self.path}")
        parts = self.path.split('/')
        print(parts)
        live_data = ExtractFeatures(parts[3])
        result = predict_model(kmeans, data=live_data)
        print(result)
        print(result['Cluster'][0])
        if result['Cluster'][0] == "Cluster 1":
            print("Intrusion detected")
        if len(parts) >= 2:
            self.proxy_request('http://' + parts[2] + '/')
        else:
            super().do_GET()
    def do_POST(self):
        self.do_GET()
    def do_CONNECT(self):
        # Extract the host and port from the path
        address, port = self.path.split(":")
        port = int(port)
        
        try:
            # Create a socket to connect to the destination server
            with socket.create_connection((address, port)) as sock:
                # Respond with a 200 Connection Established status
                self.send_response(200, "Connection Established")
                self.end_headers()
                
                # Connect the client's connection to the destination
                self._relay_data(self.connection, sock)
        except Exception as e:
            print(f"Error handling CONNECT request: {e}")
            self.send_error(502, "Bad Gateway")

    def proxy_request(self, url):
        try:
            response = request.urlopen(url)
        except error.HTTPError as e:
            print('Error:', e)
            self.send_response_only(e.code)
            self.end_headers()
            return
        self.send_response_only(response.status)
        for name, value in response.headers.items():
            self.send_header(name, value)
        self.end_headers()
        self.copyfile(response, self.wfile)



SimpleHTTPProxy.set_routes({'proxy_route': 'http://13.60.232.240:5000/'})
with HTTPServer(('127.0.0.1', 8080), SimpleHTTPProxy) as httpd:
    host, port = httpd.socket.getsockname()
    print(f'Listening on http://{host}:{port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting")
