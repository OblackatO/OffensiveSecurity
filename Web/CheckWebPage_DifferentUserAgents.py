import requests
import hashlib 

user_agents = { 'Chrome on Windows 8.1' : 'Mozilla/5.0 (Windows NT6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/40.0.2214.115 Safari/537.36','Safari on iOS' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0Mobile/12B466 Safari/600.1.4','IE6 on Windows XP' : 'Mozilla/5.0 (Windows; U; MSIE 6.0; Windows\
NT 5.1; SV1; .NET CLR 2.0.50727)','Googlebot' : 'Mozilla/5.0 (compatible; Googlebot/2.1;\
+http://www.google.com/bot.html)' }

responses = {}
for name, agent in user_agents.items():
	headers = {'User-Agent' : agent}
	req = requests.get('http://packtpub.com', headers=headers)
	responses[name] = req

md5s = {}
for name, response in responses.items():
	md5s[name] = hashlib.md5(response.text.encode('utf-8')).hexdigest()
	for name,md5 in md5s.iteritems():
		if name != 'Chrome on Windows 8.1':
			if md5 != md5s['Chrome on Windows 8.1']:
				print (name, 'differs from baseline')
			else:
				print ('No alternative site found via User-Agentspoofing:', md5)


"""
Verifys if the website provides a different web_page content by spoofing different user-agents
converts the webpage content in md5 and hex to be faster and easier to compare them. 
Could be used to check if there are different vulnerabilities in the different versions of the website. 
Check the user-agents and change them for computer(windows,macox,linux), iphone and android for the main 
browsers. 
"""


