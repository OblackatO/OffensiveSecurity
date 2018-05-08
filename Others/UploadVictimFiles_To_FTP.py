from ftplib import FTP
import time,os

user = sys.argv[1]
pw = sys.argv[2]

ftp = FTP("127.0.0.1", user, pw)
filescheck = "aa"
loop = 0
up = "../"

while 1:
	files = os.listdir("./"+(up*loop))
	print (files)
	
	for f in files:
		try:
			fiile = open(f, 'rb')
			ftp.storbinary('STOR ftpfiles/00'+str(f), fiile)
			fiile.close()
		except:
			pass
	if filescheck == files:  #see comment 1   
		break
	else:
		filescheck = files
		loop = loop+1
		time.sleep(10)

ftp.close()

"""
comment 1 : 
when we arrive at '/' which is the root folder, there are no more folder to go
up into, we'll be stuck at the root folder and the filescheck
will equal the files and the script breaks to avoid redundancy. 
""" 