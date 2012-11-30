import re

matchers = (
r"""
  (?P<plaintiff>.+)[ ]+ 
  (v[.])[ ]+
  (?P<defendant>.+),
  [ ]+
  (?P<volume>\d+)[ ]+
  (?P<reporter>[a-z]+)[ ]+
  (?P<page>\d+)[ ]+
  [(]
  (?P<year>\d{4})
  [)]
  [.]?
""",
)

keys = (
    "plaintiff",
    "defendant",
    "volume",
    "reporter",
    "page",
    "year",
)

regs = [re.compile(m, re.I | re.X | re.DEBUG) for m in matchers]


def search_for_match(text):
    match = None
    for r in regs:
        match = r.match(text)
        if match:
            break
    return match

def main():
    print(regs)
    match = search_for_match("willy nelson v. johnny cash, 23 oldman 435 (1956).")
    if not match:
        raise SystemExit(-1)
    
    for key in keys:
        print('{:>10}: {}'.format(key, match.group(key)))
    print(repr(match.group(0)))

if __name__ == '__main__':
    main()
