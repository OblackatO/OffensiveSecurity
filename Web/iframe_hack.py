import requests
from selenium import webdriver

URL = 'WEBsite'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
req = requests.get(URL,headers=headers)

try:
	xframe = req.headers['x-frame-options']
	print ('X-FRAME-OPTIONS:', xframe , 'present, clickjacking not likely possible')
except:
	print ('[>]Header: X-FRAME-OPTIONS missing.')
	print ('[>]Attempting clickjacking.')
	html = '''
	<html>
	<body>
	<iframe src="'''+URL+'''" height='600px' width='800px'></iframe>
	</body>
	</html>'''
	
	html_filename = 'clickjack.html'
	f = open(html_filename, 'w+')
	f.write(html)
	f.close()
	path_to_phantom = "PATH to phantom drive"
	browser = webdriver.PhantomJS(path_to_phantom)
	browser.get('clickjack.html')
	if 'forbidden' in browser.page_source:
		print ('[>]Clickjacking forbidden by X-FRAME-OPTIONS.')
	else : 
		print('[>]Clickjacking possible. Check ckickjack.html to confirm.')
	browser.quit()

"""
This script checks if it is possible to create a iframe of a certain website or not. 
Check guide for clickjacking with python
"""
