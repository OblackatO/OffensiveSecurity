import requests
import sys
from bs4 import BeautifulSoup, SoupStrainer
url = "http://127.0.0.1/xss/medium/guestbook2.php"
url2 = "http://127.0.0.1/xss/medium/addguestbook2.php"
url3 = "http://127.0.0.1/xss/medium/viewguestbook2.php"
f = open("~/interesting-metacharacters.txt")
o = open("results.txt", 'a')

print ("Fuzzing begins!")
initial = requests.get(url)
for payload in f.readlines():
	for field in BeautifulSoup(initial.text,parse_only=SoupStrainer('input')):
		d = {}
		if field.has_attr('name'):
			if field['name'].lower() == "submit":
			d[field['name']] = "submit"
		else:
			d[field['name']] = payload
		req = requests.post(url2, data=d)
		response = requests.get(url3)
		o.write("Payload: "+ payload +"\r\n")
		o.write(response.text+"\r\n")

print ("Fuzzing has ended")

"""
Fuzzing website, write results to a txt file and manually analyze them.
List used to for metacharacters : https://github.com/fuzzdb-project/fuzzdb/blob/master/attack/all-attacks all-attacks-xplatform.txt

Fuzzing definition: "Fuzzing is the usually automated process of entering random data into a program and analyzing the results to find potentially exploitable bugs."
"""
