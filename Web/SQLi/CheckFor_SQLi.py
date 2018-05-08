import requests
url = "urs_here"
initial = "'"
print ("Testing "+ url)

first = requests.post(url+initial)
first = first.text.lower()
if "mysql" in first:
	print ("Injectable MySQL detected")
elif "native client" in first:
	print ("Injectable MSSQL detected")
elif "syntax error" in first:
	print ("Injectable PostGRES detected")
elif "ORA" in first:
	print ("Injectable Oracle detected")
else:
	print ("Not Injectable J J")


"""
This can be adapted to check in every link found on a webpage. 
Regex can be used to search for input fields. 
"""