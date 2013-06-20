"""
Converts the table of case citation data from the cornell website:

http://www.law.cornell.edu/citation/

Into computer friendly XML.

Infile = case_citations.txt
Outfile = case_citations.xml
"""
from lxml import etree as ET

INFILE_NAME = 'case_citations.txt'
OUTFILE_NAME = 'case_citations.xml'

def preprocess(text):
    """
    convert the text into a list of line strings.
    """
    lines = text.splitlines()

    # strip whitespace
    lines = [l.strip() for l in lines]

    # kill comments 
    lines = filter(lambda l: not l.startswith('#'), lines)

    # filter out blank lines
    lines = filter(lambda l: len(l) > 0, lines)

    return lines



def build_data(lines):
    """
    Build a dictionary that will be converted into xml. main key of
    the dictionary will be a <Section> node of the xml file. 
    """
    current_section = ""
    data = {}

    for line in lines:
        if not current_section or \
                line in sections:

            current_section = line
            data[current_section] = {'citations' : [], 'comments' : []}
            continue
    
        if line.startswith('*'):
            data[current_section]['comments'].append(line)
            continue
        
        data[current_section]['citations'].append(line)
        
    return data



ONE_STAR = '*'
TWO_STARS = '**'
def build_xml(data):
    """
    Take the data dictionary and convert it to a sane XML representation.
    """
    root = ET.Element("CitationData")
    root.set('type', 'case')

    for section, elems in data.items():
        sect_node = ET.SubElement(root, "Section")
        sect_node.set("id", section);
        for cite in elems['citations']:
            cite_node = ET.SubElement(sect_node, "Citation")

            if cite.endswith(TWO_STARS): 
                cite = cite[:-2]
                cite_node.set("comment", "2")

            elif cite.endswith(ONE_STAR): 
                cite = cite[:-1]
                cite_node.set("comment", "1")


            cite_node.text = cite

        for comment in elems['comments']:
            comment_node = ET.SubElement(sect_node, "Comment")

            if comment.startswith(TWO_STARS):
                comment_node.set('id', '2')
                comment = comment[2:]
            elif comment.startswith(ONE_STAR):
                comment_node.set('id', '1')
                comment = comment[1:]


            comment_node.text = comment.strip()
            
    return root



def read_text(filepath):
    """
    Obtain the text string from the file at filepath.
    """
    with open(filepath, 'r') as infile:
        text = infile.read()
    return text



def write_xml(filepath, xml):
    """
    Write the xml to filepath.
    
    XML is the root element tree node.
    """
    text = ET.tostring(xml, pretty_print=True, encoding="unicode")

    with open(filepath, 'w') as outfile:
        outfile.write(text)




def main():
    text = read_text(INFILE_NAME)
    lines = preprocess(text)
    data = build_data(lines)
    xml = build_xml(data)
    write_xml(OUTFILE_NAME, xml)


# The set of sections from the table. Some are federal courts but
# other indicate case citations for state jurisdictions.
# 
# Generated from the case_citations.txt w/iPython.
#
sections = ['Supreme Court',
 'Courts of Appeals',
 'District Courts',
 'Court of Federal Claims',
 'Bankruptcy Courts and Bankruptcy Panels',
 'Tax Court',
 'Military Service Courts of Criminal Appeals',
 'Alabama',
 'Alaska',
 'Arizona',
 'Arkansas',
 'California',
 'Colorado',
 'Connecticut',
 'Delaware',
 'District of Columbia',
 'Florida',
 'Georgia',
 'Hawaii',
 'Idaho',
 'Illinois',
 'Indiana',
 'Iowa',
 'Kansas',
 'Louisiana',
 'Maine',
 'Maryland',
 'Massachusetts',
 'Michigan',
 'Minnesota',
 'Mississippi',
 'Missouri',
 'Montana',
 'Nebraska',
 'Nevada',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'New York',
 'North Carolina',
 'North Dakota',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Vermont',
 'Virginia',
 'Washington',
 'West Virginia',
 'Wisconsin',
 'Wyoming']


if __name__ == '__main__':
    main()
