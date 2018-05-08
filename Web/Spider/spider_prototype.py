from bs4 import BeautifulSoup 
import urllib.request as ur 
import sys 

urls = []

def get_links(website):
	try:
		print('im parsing this site',website)
		web_page = ur.urlopen(website).read() 
		bsi = BeautifulSoup(web_page,'lxml')
		if bsi == NoneType : 
			pass
		else : 
			for link in bsi.find_all('a'):
				link = link.get('href')
				if 'http' in link[:4] :
					urls.append(link)
				if '/' in link[:2] :
					urls.append(website+link)
	except Exception as e:
		print(e)
		pass

get_links(sys.argv[1])
"""
for item in urls : 
	get_links(item)

print(urls)
urls2 = set(urls)
print('with set,',urls2)
"""
"""
READ_ME : 
This script is supposed to be a spider. It would be useful to 
parse all links of a website and the links provided by each link, 
till no more links are found. I tried to use a while loop and adding
/removing links from a list, and while there were elements on this
list the while loop wouldn't stop. Anyway this could really take a lot of time
, multithreading or multiprocessing should be used. I let the script 
able to only make a parse for links on the webpage,without looking for more
links in the found links. Do not forget to organize the list to remove
repeated items. See set() function.
""" 