#!/usr/bin/env python3
"""Check full Jekyll output; run after scripts/jekyll.sh build."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
html = (SITE / 'index.html').read_text()
assert html.lstrip().lower().startswith('<!doctype html>'), 'Front matter leaked into homepage'
assert 'noindex' not in html and '{{' not in html and '{%' not in html, 'Unrendered/preview homepage'
for name in ('README.md', 'AGENTS.md', 'scripts', 'tests', 'Gemfile', 'Gemfile.lock', '.git'):
    assert not (SITE / name).exists(), f'Development-only path published: {name}'

class Resources(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key not in ('href', 'src') or not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            path = (SITE / unquote(url.path).lstrip('/')).resolve()
            assert path.is_relative_to(SITE.resolve()) and path.is_file(), f'Missing built resource: {value}'
            relative = path.relative_to(SITE)
            assert path.read_bytes() == (ROOT / relative).read_bytes(), f'Changed resource: {relative}'
Resources().feed(html)
projects = list((ROOT / '_projects').glob('*.md')) + list((ROOT / '_projects').glob('*.html'))
for project in projects:
    output = SITE / 'projects' / (project.stem + '.html')
    assert output.is_file(), f'Legacy project not generated: {project.name}'
    assert '{{' not in output.read_text() and '{%' not in output.read_text(), f'Unrendered template: {project.name}'
print(f'PASS: generated homepage and assets, {len(projects)} legacy project pages, no development files published.')
