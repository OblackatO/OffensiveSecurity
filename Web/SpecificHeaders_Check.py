import requests
req = requests.get('http://packtpub.com')
headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code']

for header in headers:
	try:
		result = req.headers[header]
		print ('%s: %s') % (header, result)
	except Exception as error:
		print ('%s: Not found') % header


"""
Checks for specific headers provided by the user. 
Can be extended to check for vulnerabilities 
"""
