#!/usr/bin/env python3
"""Dependency-free homepage preview, not a full Jekyll renderer."""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        target = (ROOT / path.lstrip('/')).resolve()
        allowed = path in ('/', '/index.html', '/research-resume.pdf') or path.startswith(('/assets/', '/libs/'))
        if not allowed or not target.is_relative_to(ROOT) or any(p.startswith('.') for p in Path(path).parts):
            self.send_error(404)
            return None
        if path in ('/', '/index.html'):
            import io
            html = (ROOT / 'index.html').read_text()
            if html.startswith('---\n'):
                html = html.split('---\n', 2)[2]
            html = html.replace('</head>', '<meta name="robots" content="noindex, nofollow"></head>')
            data = html.encode()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            return io.BytesIO(data)
        if not target.is_file():
            self.send_error(404)
            return None
        return super().send_head()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8766)
    args = parser.parse_args()
    with ThreadingHTTPServer(('127.0.0.1', args.port), PreviewHandler) as server:
        print(f'Homepage preview: http://127.0.0.1:{args.port}/ (not a full Jekyll build)', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
