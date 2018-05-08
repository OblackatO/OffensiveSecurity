import urllib.request as ur
import sys

list_files = ['index','page1','page2']

url = sys.argv[1]
format_1 = sys.argv[2]
got_files = False

if '/' not in url[-1:]:
	url = url + '/'

for item in list_files:
	try:
		web_code = ur.urlopen(url+item+format_1).read()
		if web_code.code() == 200 :
			got_files = True
			print('[>]File',item+format_1,'exists.')
		else : 
			pass 
	except Exception as e :
		if '404' in str(e) :
			pass
		else :
			print('[!]Not 404 error:',e)

if got_files == False :
	print('[!]No files available.') 

"""
Searches for files in the specified url and format. The list of files can
be extended. 
"""
