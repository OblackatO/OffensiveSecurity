import requests
url = 'http://www.packtpub.com/'
req = requests.get(url)

if req.cookies:
	print ('Initial cookie state:', req.cookies)
	cookie_req = requests.post(url, cookies=req.cookies,auth=('user1', 'supersecretpasswordhere'))
	print ('Authenticated cookie state:', cookie_req.cookies)

if req.cookies == cookie_req.cookies:
	print ('Session fixation vulnerability identified')

"""
I was not getting any cookies with connecting to a webpage. 
More details on script "CheckSecure_Cookies.py". 
I will try do this with phantomJS.
See the concept here : https://www.owasp.org/index.php/Session_fixation
""