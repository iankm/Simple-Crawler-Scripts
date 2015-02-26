# Goes through URLs and reads information such as
# **materials**, price, **popularity**
# organizes them in a document.

import urllib2
import urlparse
import re
from bs4 import BeautifulSoup, SoupStrainer
import sys

URLS = ['http://gap.com/']

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


address = 0 # Global place in dictionary
CLOTHING = dict() # Creates a dictionary for clothing

class Item:
    def __init__(self, name, price, source):
    	self.n = name
        self.p = price
        self.s = source





# Works only for gap.com as of now
def crawl(url):
    request = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(request)
    text= response.read()
    response.close()
    soup = BeautifulSoup(text)

    for tag in soup.findAll('a', href=re.compile('products')):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        newRequest = urllib2.Request(tag['href'], headers=hdr)
        newResponse = urllib2.urlopen(newRequest)
        newText= newResponse.read()
        newResponse.close()
        newText = newText.decode('utf8')
        newSoup = BeautifulSoup(newText)
        addClothes(newSoup, tag['href'])

        
def addClothes(newSoup, url):
    global address
    for clothing in newSoup.findAll('a', class_=re.compile('productItemName')):
        name = ''.join(clothing.findAll(text=True))
        price = ''.join(clothing.findNext('span', class_=re.compile('priceDisplay'), text=True))
        newItem = Item(name, price, url)
        CLOTHING[address] = newItem
        address = address + 1

def printClothes():
    for key in CLOTHING:
        if (key == 0) or (CLOTHING[key].s != CLOTHING[key-1].s):
            print "\n" + CLOTHING[key].s + "\n"
        print (CLOTHING[key].n, CLOTHING[key].p, CLOTHING[key].s)

"""def getAveragePrice():
    pricesum = 0
    numitems = 0
    for key in CLOTHING:
        price = int(CLOTHING[key].p.split('$')[0])
        pricesum = pricesum + price
        numitems = numitems + 1

    print pricesum/numitems"""

def main():
    for i in URLS:
        crawl(i)

    printClothes()


if __name__ == "__main__":
	main()
