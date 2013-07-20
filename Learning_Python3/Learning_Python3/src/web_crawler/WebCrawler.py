#### WEB CRAWLER
def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote +1)
	url = page[start_quote + 1 : end_quote]
	return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
            
            	
def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:	
			break
	return links
	
# tocrawl is a list of pages left to crawl, want to get rid
# of pages as we have tocrawled them, adding it to crawled
# crawled list of pages crawled starts as empty list
		
def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []	
	while tocrawl:
		page = tocrawl.pop() #remove last element of tocrawl
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index,page,content)
			union(tocrawl, get_all_links(content))
			crawled.append(page)
	return index
	
# UNIT 4: Data Structures

def add_to_index(index, keyword, url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return 
	index.append([keyword,[url]])
	
def lookup(index, keyword):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return []
	
# Building the Web Index

def add_page_to_index(index, url, content):
	keyword = content.split()
	for keyword in keyword:
		add_to_index(index,keyword,url)

def get_page(url):
	try:
		import urlib
		return urllib.urlopen(url).read
	except:
			return""
get_page('http://risk.net')
