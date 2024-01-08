import http.server
import socketserver
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set the desired port (e.g., 8000)
port = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Serving at http://localhost:{port}")
    httpd.serve_forever()


