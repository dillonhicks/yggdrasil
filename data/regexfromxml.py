import re

from xml.etree import ElementTree

TESTFILE = 'regularexpressions.xml'



def build_component(elem):
    name = ''
    occurance = ''
    
    
    try: name = elem.attrib['name']
    except KeyError: pass
    try: occurance = elem.attrib['occurance']
    except KeyError: pass

    if elem.tag == 'anything':
        match = '.'
    elif elem.tag == 'exactly':
        match = elem.attrib['match']

    tpl = ''
    if name:
        tpl = '(?P<{}>({}){})'
    else:
        tpl = '(({}){})'
    

    regex_component = tpl.format(name, match, occurance)
    return regex_component


def build_regex(text):
    root = ElementTree.fromstring(text)

    components = [ build_component(c) for c in root ]
    pattern = ''.join(components)
    print(re.match(pattern, "blah blah blah fdafdsa dDillon"))


def main():
    text = ""
    with open(TESTFILE, 'r') as frank:
        text = frank.read()
        print(text)

    build_regex(text)


if __name__ == '__main__':
    main()
