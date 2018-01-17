from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
#Retrieve HTML string from the URL
html = urlopen("https://movie.douban.com/chart")
bs=BeautifulSoup(html,from_encoding="utf8")
#print bs.original_encoding
#contentlist=bs.findAll("span",{"class":"pl"})
def getinterlink(bs):
	linkinter=set()
	linkinterlist=bs.findAll("a",{"href":re.compile("https://movie.douban.com/subject/[0-9]+/$")})
	for link in linkinterlist:
		linkinter.add(link['href'])
	print len(linkinter)
	return linkinter
	
	

def getexlink(bs):
	linkex = set()
 	getexlist=bs.findAll("a",{"href":re.compile("^(/)")})
	#print len(getexlist)
	for link in getexlist:
		linkex.add(link['href'])
	print len(linkex)
	return linkex
	
for link in getinterlink(bs):
	print link

for link in getexlink(bs):
	print link



