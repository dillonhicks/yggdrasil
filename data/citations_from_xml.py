from lxml import etree as ET

INFILE_NAME = "case_citations.xml"

def main():
    tree = ET.parse(INFILE_NAME)
    cite_nodes = tree.xpath("/CitationData/Section[@id='Supreme Court']/Citation")
    cites = [c.text for c in cite_nodes]
    print('\n'.join(cites))

if __name__ == '__main__':
    main()
