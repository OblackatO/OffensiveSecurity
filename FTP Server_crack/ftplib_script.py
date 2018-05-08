"""from ftplib import *

ftpinstance = ftplib('ftps://94.252.12.2')
ftpinstance.login('Pedro','Eskecime123')
print (ftpinstance.getwelcome())
ftpinstance.close()"""
from ftplib import FTP
try:
	ftp = FTP_TLS('ftp.debian.org')     # connect to host, default port
	ftp.login()                     # user anonymous, passwd anonymous@
	'230 Login successful.'
	ftp.cwd('debian')               # change into "debian" directory
	ftp.retrlines('LIST')
except Exception as e:
	print (e)           # list directory contents