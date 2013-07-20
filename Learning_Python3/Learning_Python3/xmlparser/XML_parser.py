'''
Created on Jul 4, 2013

@author: Aleks
'''
from urllib.request import urlopen
from xml.etree.ElementTree import parse

def main():
    #Download the RSS feed and parse it
    u = urlopen('http://planet.python.org/rss20.xml')
    doc = parse(u)
    
    #Extract and output tags of interest
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')
        
        print(title)
        print(date)
        print(link)
        print()

if __name__ == '__main__': main()
    