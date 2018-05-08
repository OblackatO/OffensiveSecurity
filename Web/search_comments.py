import requests as R
import sys,re 
from bs4 import BeautifulSoup

urls = []

web_page = sys.argv[1]

def get_links(website):
	page_code = R.get(web_page)
	bi = BeautifulSoup(page_code.text,'lxml')
	for item in bi.find_all('a'):
		item = item.get('href')
		if 'http' in item[:4] :
			urls.append(item)
		if '/' in item[:1] :
			item = website + item
			urls.append(item)

def search_comments(url) :
	print('On this url:',url) 
	page_code = R.get(url)
	results = re.findall("<!--(.*)-->",page_code.text) # results = re.findall("<!--.*-->",string1)
	if results != [] :
		for result in results : 
			print('[>]Comment:',result)
	else : 
		print('[>]Did not find any comments on the web page.')

def main():
	get_links(web_page)
	for url in urls : 
		search_comments(url)

main()

"""
Finds comments in a webpage. In line 23, if <!--(.*)--> replaced by results = re.findall <!--[.*]--> 
will match the chars into the [] and not their meaning in the re library, must use () for that. 
""" 
