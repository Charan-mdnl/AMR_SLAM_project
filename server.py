import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def open_browser():
    time.sleep(1.5)  # Wait for server to boot up
    url = f"http://localhost:{PORT}/index.html"
    print(f"\n[Simulator] Automatically opening browser to: {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    # Start browser-opener thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    Handler = http.server.SimpleHTTPRequestHandler
    # Allow port reuse to avoid 'Address already in use' errors
    socketserver.TCPServer.allow_reuse_address = True
    
    print(f"[Simulator] Starting localhost web server on port {PORT}...")
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"[Simulator] Web server is active. Press Ctrl+C to stop.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Simulator] Web server stopped.")
    except Exception as e:
        print(f"\n[Simulator] Error starting server: {e}")
        print("[Simulator] Trying port 8001 instead...")
        PORT = 8001
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
