import requests,sys

list_requets = ['GET','HEAD','POST','PUT','TRACE','OPTIONS','DELETE','CONNECT','HOME_MADE_METHOD']

for request in list_requets : 
	request1 = requests.request(request,sys.argv[1])
	if request == 'TRACE' and 'TRACE / HTTP/1.1' in request1.text : 
		print('[>]Possible XST vulnerability',request,request1.status_code,request1.reason)
	elif request == list_requets[8] and '200' in str(request1.status_code) : 
		print('[>]Unexcepted method accepted. Check Firewall bypass.',request,request1.status_code,request1.reason)
	else:
		print(request,request1.status_code,request1.reason) 

"""
If a website X responds or allows some request types that it should not, it might has a vulnerability
that can be exploited.
"""
