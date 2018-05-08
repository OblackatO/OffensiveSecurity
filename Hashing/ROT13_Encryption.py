from string import ascii_lowercase, ascii_uppercase

#ascii_lower : contains all lower case chars of the alphabet
#ascii_upper : same thing, but upper case chars 
#makestrans('aeiou','12345'), replace the chars of the  first argument
#with the chars of the second one, for example a becomes 1 , e becomes
# w etc ...

def rot13_encrypt(message):
	message = message.lower().encode()
	lower_chars = bytes.maketrans(ascii_lowercase.encode(),ascii_lowercase[13:].encode()+ascii_lowercase[:13].encode())
	#upper_chars = makestrans(ascii_uppercase,ascii_lowercase[13:]) # If upper case chars must stay.
	return message.translate(lower_chars)#.translate(upper_chars)


print(rot13_encrypt('This is an example of encoding in Python'))
