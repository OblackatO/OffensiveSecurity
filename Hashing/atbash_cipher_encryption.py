from string import ascii_lowercase 

alphabet = ascii_lowercase
inverted_alphabet = ''

for x in range(len(alphabet)):
	x = x + 1  # because it start in 0, and when we are starting at the opposite side of a string, 0 does not count.
	char = alphabet[-x] 
	inverted_alphabet += char

def translate_atbash(message): 
	translation_function = bytes.maketrans(alphabet.encode(),inverted_alphabet.encode())
	return message.translate(translation_function)

message = 'This is a test to be translated to atbash cipher.'.lower().encode()
print(translate_atbash(message))

