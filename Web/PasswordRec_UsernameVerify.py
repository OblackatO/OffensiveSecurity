import urllib.request as ur 
import urllib.parse as up
import sys

webpage = sys.argv[1]
request = ur.Request(webpage,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})
data = up.encode({'name':'testi1_kl@hotmail.com'})
web_code = ur.urlopen(request,data).read()
print(webpage)

"""
This idea of this script was to make requests in webpage that are supposed 
to help users recover their passwords. In case the email or username
are incorrect, the page should give us an error and that tells us the username
does not exist, in the contrary we know the username exists. 
Maybe it would be a good idea to use Requests to do this. 
"""


 