import hashlib 

string = 'This is a message that goes to md5.'
md5_string = hashlib.md5(string.encode())
print('[>]Encrypted message',md5_string.digest(),'\n'
	  '[>]Message hex:',md5_string.hexdigest()
	  )

"""
The same thing goes for sha1, sha128, sha256
Perhaps make a script to calculate all the hashes at once.
"""

