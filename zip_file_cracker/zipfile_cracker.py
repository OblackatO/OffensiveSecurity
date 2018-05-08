import zipfile ,re ,os

def crack_ZipFile(password):
	try:
		password = str(password).encode('utf-8')
		password = bytes(password)
		zf.extractall(pwd=password)
		print('[>]Password match found:',password)
		os._exit(0)
	except Exception as e:
		if re.search('Bad password|bad|incorrect password',str(e),re.I) is not None:
			print('[!]Bad password:',password)

def main(file,dict1):
	global zf
	zf = zipfile.ZipFile(file)
	dictf = open(dict1,'r')
	lines = dictf.readlines()
	dictf.close()
	for line in lines :
		line = line.strip()
		crack_ZipFile(line)

main('peace2.zip','dict')



