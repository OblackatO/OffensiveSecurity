import bcrypt

password = input('[>]Enter password to store in db:')
key_to_store = bcrypt.hashpw('test1'.encode(),bcrypt.gensalt(14))
print('generated key:',key_to_store)

if bcrypt.checkpw('test1'.encode(),key_to_store):
	print('Password match')
else : 
	pass

"""
bcrypt. Type of encryption based on the blowfish cipher. 
Good for bruteforce attacks, because it takes time to generate,and
the generation, apparently, does not depend on the computer ressources.
"""
