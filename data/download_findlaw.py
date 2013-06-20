"""
Crawl Findlaw
"""

FINDLAW_URL = "http://www.findlaw.com/casecode/"

from urllib.request import urlopen

from bs4 import BeautifulSoup

def main():
    page = urlopen(FINDLAW_URL)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html)
    print(soup.prettify())

if __name__ == '__main__':
    main()


