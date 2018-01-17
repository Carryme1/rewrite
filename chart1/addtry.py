from urllib2 import urlopen,HTTPError
from bs4 import BeautifulSoup
def gettitle(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		return None
	try:
		obj=BeautifulSoup(html,from_encoding="utf8")
		title=(obj.title).encode('gb18030')
	except AttributeError as e:
		return None
	return title	
title=gettitle('http://www.baidu.com')
if title == None:
	print("Title could not be found")
else:
	print title
		
	
