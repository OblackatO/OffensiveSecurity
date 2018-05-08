import requests
import re
from bs4 import BeautifulSoup
import sys

scripts = []

def Jquery_actual_version(link):
	version2 = []
	version3 = []
	page_code = requests.get(link).text
	search_versions = re.findall('JQuery Core [0-9.{3}]+',page_code,re.I)
	for x in range(len(search_versions)) : 
		item = search_versions[x].strip('jQuery Core')
		if '2' in item[0] :
			version2.append(item)
		elif '3' in item[0] :
			version3.append(item)
	version2.sort()
	version3.sort()
	return version2[-1],version3[-1]

jquery_lastv = Jquery_actual_version('https://code.jquery.com/jquery/')

if len(sys.argv) != 2:
	print ("usage: %s url" % (sys.argv[0]))
	sys.exit(0)

tarurl = sys.argv[1]
headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'}
url = requests.get(tarurl, headers=headers) #Needed to adapt for big websites like facebook and amazon.
soup = BeautifulSoup(url.text,'lxml')

for line in soup.find_all('script'):
	newline = line.get('src')
	if newline != None:
		scripts.append(newline)
	else : 
		pass

if scripts != [] :
	for script in scripts:
		if "jquery" in str(script).lower():
			if 'http' not in script[:4]:
				script = tarurl+'/'+script
			url = requests.get(script)
			versions = re.findall('[0-9a-zA-Z._:-].*',url.text) #r'\d[0-9a-zA-Z._:-]+
			if versions != [] : 
				if versions[0] == jquery_lastv[0] or versions[0] == jquery_lastv[1]: #Change to actual version
					print ('[>]Up to date:',script)
				else:
					print ('[!]Out of date:',script)
					print ("[>]Version detected: "+versions[0])
			else : 
				print('[!]No versions found for:',script)
else :
	print('No links available.')

"""
The Jquery_actual_version finds the lastest JQuery version and checks if it's outdated 
or not. If it is we may be able to exploit some vulnerabilities.
"""
