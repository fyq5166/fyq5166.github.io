#!/usr/bin/env python3
"""Validate the homepage's structural and content-maintenance contracts."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
class Node:
    def __init__(self, tag='', attrs=(), parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs), parent, []
    def has(self, cls):
        return cls in self.attrs.get('class', '').split()
    def descendants(self):
        for child in self.children:
            yield child
            yield from child.descendants()
    def find(self, predicate):
        return [n for n in self.descendants() if predicate(n)]
class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.root = self.current = Node(); self.feed(text)
    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.current); self.current.children.append(node)
        if tag not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):
            self.current = node
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.current.tag == tag: self.handle_endtag(tag)
    def handle_endtag(self, tag):
        node = self.current
        while node.parent:
            if node.tag == tag:
                self.current = node.parent; return
            node = node.parent

text = (ROOT / 'index.html').read_text()
root = Document(text).root
nodes = list(root.descendants()); errors = []
def check(ok, message):
    if not ok: errors.append(message)
ids = [n.attrs['id'] for n in nodes if 'id' in n.attrs]
check(len(ids)==len(set(ids)), 'Duplicate HTML IDs')
by_id = {n.attrs['id']:n for n in nodes if 'id' in n.attrs}
cards = [n for n in nodes if n.has('work-card')]
panels = [n for n in nodes if n.has('project-dialog')]
check(bool(cards) and len(cards)==len(panels), 'Work card / detail count mismatch')
card_targets=[]
for card in cards:
    triggers=card.find(lambda n:'data-dialog' in n.attrs)
    check(len(triggers)==1,'Each Work card needs exactly one detail trigger')
    card_targets += [n.attrs['data-dialog'] for n in triggers]
check(len(card_targets)==len(set(card_targets)), 'Duplicate Work card target')
check(set(card_targets)=={n.attrs.get('id') for n in panels},'Unreachable or missing project detail')
for n in nodes:
    a=n.attrs
    if 'data-dialog' in a:
        check(a['data-dialog'] in by_id and by_id[a['data-dialog']].tag=='dialog','Broken detail trigger: '+a['data-dialog'])
    if n.tag=='img':
        check(bool(a.get('alt')) and bool(a.get('width')) and bool(a.get('height')), 'Image missing alt/dimensions')
    if a.get('target')=='_blank': check('noopener' in a.get('rel',''), 'External tab link lacks noopener')
    for key in ('href','src'):
        value=a.get(key,''); url=urlsplit(value)
        if not value or url.scheme or url.netloc: continue
        if url.path:
            path=(ROOT/unquote(url.path).lstrip('/')).resolve()
            check(path.is_relative_to(ROOT) and path.exists(),'Missing local resource: '+value)
        elif url.fragment: check(unquote(url.fragment) in by_id,'Missing anchor: '+value)
for panel in panels:
    name=panel.attrs['id']; slug=name.removeprefix('detail-')
    for cls in ('detail-lead','detail-results','detail-learning','detail-actions'):
        check(len(panel.find(lambda n:n.has(cls)))==1,f'{name}: missing/duplicate {cls}')
    check(len(panel.find(lambda n:n.attrs.get('data-copy-project')==slug))==1,f'{name}: copy link slug mismatch')
    check(panel.attrs.get('aria-labelledby') in by_id,f'{name}: missing accessible title')
    resources=panel.find(lambda n:n.has('quick-resources'))
    for nav in resources:
        for link in nav.find(lambda n:n.tag=='a'):
            matches=panel.find(lambda n:n.tag=='a' and n.attrs.get('href')==link.attrs['href'])
            check(len(matches)>=2,f'{name}: header resource not in bottom resources')
check(text.startswith('---\nlayout: null\n'),'Missing Jekyll front matter')
check(not re.search(r'Local design preview|noindex|localhost|127\.0\.0\.1|data:image',text),'Preview-only content in production homepage')
check(not re.search(r'Fig(?:ure)?\.?\s*\d',text,re.I),'Hard-coded figure number')
check('const syncProjectIndex =' in text and 'data-project-count' in text,'Automatic project index missing')
check((ROOT/'research-resume.pdf').read_bytes()==(ROOT/'assets/cv/Resume_Yeqiao.pdf').read_bytes(),'Resume aliases differ')
if errors:
    raise SystemExit('\n'.join('FAIL: '+e for e in errors))
print(f'PASS: {len(cards)} projects; detail structure, resources, anchors, images and resume aliases.')
