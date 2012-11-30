import re

matchers = (
    ("filed but not decided",
     r"""                    # Match 
      (?P<plaintiff>.+)[ ]+  # anything until 'v.' 
      (v[.])[ ]+             # v.
      (?P<defendant>.+),     # Anything until 'No.'
      [ ]+                   
      No[.][ ]+                  # 'No.'
      (?P<docket>\d+[-]\d+)[ ]+  #  ###-### 
      [(]                        # '('
      (?P<jurisdiction>.+)[ ]+   # anything until 'filled'
      filled[ ]+                 # 'filled'
      (?P<month>.+)[ ]+          # anything until # or ##
      (?P<day>\d{1,2}),          # 1-2 digit day followed by comma ','
      [ ]+         
      (?P<year>\d{4})            # 4 digit year
      [)]                        # ')'
      [.]?                       # optional period '.'
      """),

    ("u.s. supreme court decision", 
     r"""                        # Match
      (?P<plaintiff>.+)[ ]+      # anything until 'v.' 
      (v[.])[ ]+                 # 'v.'
      (?P<defendant>.+),         # Anything until the first comma ','
      [ ]+                     

      (?P<volume>\d+)[ ]+        # 1 or more digits for the volume
      (?P<reporter>              # Reporter as
            (U[.]S[.])|          # U.S. or
            (S[.][ ]+Ct[.])      # S. Ct.
      ) 
      [ ]+ 
      (?P<page>\d+)              # 1 or more digits as page #

                                 # (begin optional)
      (,[ ]+                       # comma ','
        (?P<pincite>\d+)           # 1 or more digits for pincite 
      )?                         # (end optional)
                
      [ ]+
      [(]                        # '('               
      (?P<year>\d{4})            # 4 digits for the year 
      [)]                        # ')'
      [.]?                       # optional period '.'
    """),


    ("published decision", 
     r"""                        # Match
      (?P<plaintiff>.+)[ ]+      # anything until 'v.' 
      (v[.])[ ]+                 # 'v.'
      (?P<defendant>.+),         # Anything until the first comma ','
      [ ]+                     
      (?P<volume>\d+)[ ]+        # 1 or more digits for the volume
      (?P<reporter>[a-z.]+)[ ]+  # characters and '.' as name of reporter 
      (?P<page>\d+)              # 1 or more digits as page #

                                 # (begin optional)
      (,[ ]+                       # comma ','
        (?P<pincite>\d+)           # 1 or more digits for pincite 
      )?                         # (end optional)
                
      [ ]+
      [(]                        # '('               
      (?P<year>\d{4})            # 4 digits for the year 
      [)]                        # ')'
      [.]?                       # optional period '.'
    """),

)


citations = (
    "willy nelson v. johnny cash, 23 oldman 435 (1956).",
    "Charlesworth v. Mack, No. 90-345 (D. Mass. filled Sept. 18, 1990).",
    "Circuit City Stores, Inc. v. Adams, 532 U.S. 105, 123 (2001).",
)

keys = (
    "plaintiff",
    "defendant",
    "volume",
    "reporter",
    "page",
    "pincite",
    "docket",
    "jurisdiction",
    "month",
    "day",
    "year",
)

regs = [(m[0], re.compile(m[1], re.I | re.X)) for m in matchers]


def search_for_match(text):
    match = None
    for name, r in regs:
        match = r.match(text)
        if match:
            break
    return name, match, text


def parse_citations():
    key_lens = [len(k) for k in keys]
    max_len = max(key_lens) + 2
    template = '{:>' + str(max_len) + '}: {}'

    matches = [ search_for_match(cite) for cite in citations ] 
    for name, match, text in matches:
        if match is None: 
            print("Unable to match:", text)
            break

        print("Matched by:", name)

        for key in keys:
            try:
                part = match.group(key)
                if part is None: continue
                print(template.format(key, part))
            except IndexError: pass

        print(repr(match.group(0)))
        print()

def main():
    parse_citations()

if __name__ == '__main__':
    main()
