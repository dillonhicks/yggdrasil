"""
Parses citations


"""
import re

from lxml import etree as ET

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
      (?P<court>.+)[ ]+   # anything until 'filled'
      filed[ ]+                 # 'filed'
      (?P<month>.+)[ ]+          # anything until # or ##
      (?P<day>\d{1,2}),          # 1-2 digit day followed by comma ','
      [ ]+         
      (?P<year>\d{4})            # 4 digit year
      [)]                        # ')'
      [.]?                       # optional period '.'
      """),


    #
    # US Supreme Court
    # 
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

    
    #
    #
    # 
    ("published decision", 
     r"""                        # Match
      ### Parties

      (?P<plaintiff>.+)[ ]+      # anything until 'v.' 
      (v[.])[ ]+                 # 'v.'
      (?P<defendant>.+),         # Anything until the first comma ','
      [ ]+                     

      ### Reporter
      (?P<volume>\d+)[ ]+        # 1 or more digits for the volume

      (?P<reporter>              # Reporter
         (                         # [Begin Block]
          (\d+)?                     # (optional) one or more digits, followed by
          [a-z.]+                    # one or more characters and/or '.' 
          ([ ]+)?                    # (optional) whitespace
         )+                        # [End Block], the items between the block 1 or more times. 
      )                          # /Reporter

      [ ]+
      (?P<page>\d+)              # 1 or more digits as page #

                                 # (begin optional)
      (,[ ]+                       # comma ','
        (?P<pincite>\d+)           # 1 or more digits for pincite 
      )?                         # (end optional)

      ### Dates 

      [ ]+
      [(]                        # '('
      (
        (?P<court>U[.]S[.])
        [ ]+
        (?P<month>[a-z]+[.])[ ]+  # Characters + '.' one or more times
        (?P<day>\d{1,2}),[ ]+     # day as up to two digits followed by a comma      
      )?

      (?P<year>\d{4})                # 4 digits for the year 
      [)]                        # ')'

      [.]?                       # optional period '.'


    """),

)

# compile the regexes of all the matcher.
matchers = [(m[0], re.compile(m[1], re.I | re.X)) for m in matchers]


citations = [
    "willy nelson v. johnny cash, 23 oldman 435 (1956).",
    "Charlesworth v. Mack, No. 90-345 (D. Mass. filed Sept. 18, 1990).",
    "Circuit City Stores, Inc. v. Adams, 532 U.S. 105, 123 (2001).",
    "Scott v. Harris, 75 U.S.L.W. 4297 (2007).",
]


# in order that you would expect to see them in any given citation.
# Helps to format the output
keys = (
    "plaintiff",
    "defendant",
    "volume",
    "reporter",
    "page",
    "pincite",
    "docket",
    "court",
    "month",
    "day",
    "year",
)
# Get the length of all the keys
_key_lens = [len(k) for k in keys]
_max_len = max(_key_lens) + 2
FIELD_TEMPLATE = '{:>' + str(_max_len) + '}: {}'


def gen_citations():
    """
    Generator for citations from different sources.  Currently I am
    just plopping new for-yield loops for each new type I want to
    test.
    """
    for c in citations:
        yield c

    tree = ET.parse("../data/case_citations.xml")
    cite_nodes = tree.xpath("/CitationData/Section[@id='Supreme Court']/Citation")
    for c in cite_nodes:
        yield c.text



def search_for_match(text):
    """
    Iterates through the list of matchers attempting to match a
    regex to the text string.

    Returns a tuple
    (name of the matcher, the match object (or None), and the matched string)
    """
    match = None
    for name, r in matchers:
        match = r.match(text)
        if match:
            break
    return name, match, text


def parse_citations():
    
    matches = (search_for_match(cite) for cite in gen_citations()) 

    for name, match, text in matches:

        if match is None: 
            print("Unable to match:", text)
            continue

        print("Matched by:", name)

        for key in keys:
            try:
                part = match.group(key)
                if part is None: continue
                print(FIELD_TEMPLATE.format(key, part))
            except IndexError: pass

        print(repr(match.group(0)))
        print()

def main():
    parse_citations()



if __name__ == '__main__':
    main()
