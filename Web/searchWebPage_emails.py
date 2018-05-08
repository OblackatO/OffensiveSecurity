"""
("([a-z0-9!#$%&'*+\/=?^_'{|}~-]+(?:\.[a-z0-
9!#$%&'*+\/=?^_'"
"{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-
]*[a-z0-9])?(\.|"
"\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")
"""
import urllib.request as ur
import sys,re

url = sys.argv[1]

try:
	page_code = ur.urlopen(url).read()
	print(page_code.decode())
	compiled = re.compile("[0-9A-Za-z]*@[A-Za-z]*")
	find_match = re.findall(compiled,page_code.decode())
	if find_match != [] : 
		for item in find_match : 
		print('[>]Email:',item)
	else : 
		print('[!]Emails not found.')
except Exception as e: 
	print(e)

""" 
finds emails in a webpage. I used a simple regex expressions that seemed 
enought to me, but there are more complete and complex expressions that
can be used. This script will only work in a webpage without looking
for the rest of the website map.
""" 