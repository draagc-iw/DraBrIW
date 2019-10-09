import ZDraBrIW.App.Brews
from http.server import HTTPServer, BaseHTTPRequestHandler
from ZDraBrIW.Server.RequestHandler import RequestHandler

def main():
    http_server = HTTPServer(("", 8080), RequestHandler)
    print(f"Server listening on port {http_server.server_port}")
    http_server.serve_forever()

if __name__ == '__main__':
    main()
