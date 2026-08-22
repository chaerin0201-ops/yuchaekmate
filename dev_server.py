# -*- coding: utf-8 -*-
"""Local preview server that mirrors the site's Vercel routing.

`python -m http.server` serves files verbatim, so the extensionless links
in the pages 404 locally even though they work in production. This mimics
vercel.json's cleanUrls instead: /foo serves foo.html, and /foo.html
redirects to /foo the way Vercel does.

Usage: python dev_server.py [port]     (default 3456)
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3456


class CleanUrlsHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        path = self.path.split('?')[0].split('#')[0]

        if path == '/index.html':
            return self._redirect('/')
        if path.endswith('.html'):
            return self._redirect(path[:-5])

        # extensionless request -> serve the matching .html
        if not path.endswith('/') and '.' not in os.path.basename(path):
            if os.path.isfile(os.path.join(ROOT, path.lstrip('/') + '.html')):
                self.path = path + '.html'

        return super().do_GET()

    def end_headers(self):
        # Without this the browser caches CSS/JS between edits and the preview
        # silently shows the previous version.
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

    def _redirect(self, location):
        self.send_response(308)
        self.send_header('Location', location)
        self.end_headers()

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    print(f'Serving {ROOT} on http://localhost:{PORT} (cleanUrls)')
    sys.stdout.flush()
    ThreadingHTTPServer(('127.0.0.1', PORT), CleanUrlsHandler).serve_forever()
