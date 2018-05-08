import requests,sys

headers = {'Chrome on Windows 8.1' : 'Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/40.0.2214.115 Safari/537.36'}

request = requests.Session()
r1 = request.get(sys.argv[1],headers=headers)
print('[>]Cookies.')
for cookie in r1.cookies : 
	if not cookie.secure : 
		cookie.secure = 'False'
	else :
		cookie.secure = 'True'
	if 'httponly' in cookie._rest.keys() : 
		cookie.httponly = 'True'
	else : 
		cookie.httponly = 'False'
	if cookie.domain_initial_dot : 
		cookie.domain_initial_dot = 'True' #defines a loosly defined domain. see note 1 
	
	print(
		'[>]Name:',cookie.name+'\n'
		'[>]Value:',cookie.value+'\n'
		'[>]Secure:',cookie.secure+'\n'
		'[>]HTTP_Only:',cookie.httponly+'\n'
		'[>]Domain_Initial_Dot:',cookie.domain_initial_dot\
		 )


"""
Note 1 : If the domain attribute of the cookie starts with a dot, it indicates the cookie is used
across all subdomains and therefore possibly visible beyond the intended scope.

Note 2 : Colors on the terminal : 
Also note that the \x1b[31m code is a special ANSI escape code used to change the
color of the terminal font. Here, we've highlighted the headers that are insecure in red.
The \x1b[39;49m code resets the color back to default. See the Wikipedia page on ANSI
for more information at http://en.wikipedia.org/wiki/ANSI_escape_code .

Note 3 : Certain frameworks also store information in the cookie, for example,
PHP creates a cookies called PHPSESSION, which is used to store session data. Therefore,
the presence of this data indicates the use of PHP, and the server can then be enumerated
further in an attempt to test it for known PHP vulnerabilities.

""" 
