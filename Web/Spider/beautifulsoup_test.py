from bs4 import BeautifulSoup 
import urllib.request as ur 
import sys 

urls = []

def get_links(website):
	try:
		web_page = ur.urlopen(website).read() 
		bsi = BeautifulSoup(web_page,'lxml')
		for link in bsi.find_all('a'):
			link = link.get('href')
			if 'http' in link[:4]:
				urls.append(link)
			if '/' in link[:2]:
				urls.append(website+link)
	except Exception as e:
		pass

get_links(sys.argv[1])

"""
while len(urls) > 0  :    
	for item in urls:
		urls.remove(item)
		print(len(urls)) 
		get_links(item)

for item in urls : 
	print('[>]',item)
"""
