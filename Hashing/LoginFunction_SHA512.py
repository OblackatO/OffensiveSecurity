import hashlib,uuid,sys

def new_password_username(user,password):
	salt = uuid.uuid4().hex
	user = hashlib.sha512(user.encode())
	print('this is the salt:',salt)
	file_userd = open('fileu1.txt','a')
	file_userd.write(user.hexdigest()+':'+salt)
	file_userd.close()
	password = salt + password
	password = hashlib.sha512(password.encode())
	file_passwd = open('filep1.txt','a')
	file_passwd.write(password.hexdigest())
	file_passwd.close()

def login(user,password):
	got_user = False
	file1u = open('fileu1.txt','r').readlines()
	user = hashlib.sha512(user.encode())
	user = user.hexdigest().strip()
	for line in file1u : 
		if user in line : 
			user,salt = line.split(':')
			print('[>]User is valid, checking password.')#feedback given just for experiments.
			print('user:',user,'salt',salt)
			got_user = True
	if got_user != True : 
		sys.exit('[!]Try again.')
	file1p = open('filep1.txt','r').read()
	password = salt.strip()+password
	password = hashlib.sha512(password.encode())
	if password.hexdigest() in file1p : 
		print('[>]Password validated.Authorization granted.')

def main() : 
	user = input('[>]Enter your username:')
	password = input('[>]Enter your password:')
	login(user,password)

main()

"""
Instead of hidding the salt and password together. I hide the salt 
with the user name. The username is encrypted with sha512. The login
function checks if the user exists, get the salt in the user's file
and use it to hash the provided password, finally we check if it exists
in the password file db. 

Perhaps it would be a good idea to hash the user in the db with a salt 
saved in the password file of the corresponding user, and the salt of the 
password in the user's files. 

example :

hashed_user1 : salt_for_pass1
hashed_pass1 : salt_for_user1 

Do not forget to add lib to hide pass being written. 
"""
