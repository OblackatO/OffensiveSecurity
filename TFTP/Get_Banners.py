#!/usr/bin/env python
import sys,socket,argparse

def check_banners(host):
	ports = [21,22,23]
	file1 = open('Banners_Info.txt','w')
	for port in ports: 
		try:
			socket.setdefaulttimeout(1)
			if '.' in host :
				print '[>]IPv4 detected.'
				s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			if ':' in host : 
				print '[>]IPv6 detected.'
				s1 = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
			s1.connect((host,port))
			output = s1.recv(1024)
			try :
				output = output.decode()
			except:
				pass
			to_write = '[>]Banner for '+str(host)+' on port '+str(port)+ ': '+output
			print to_write
			file1.write(to_write)
		except :
			pass
		finally:
			s1.close()
	file1.close()
	
def main_arguments():
	usage = "Gets the banners of the hosts which have ports 21,22 or 23 opened.\
 the banners will be saved in a txt file in the current folder.The user can then use the banners to get the\
 hosts' names and finally use them in the Get_Backup.py program. Several hosts can be specified at once."+'\n'+\
 "Example : "+sys.argv[0]+" -vulnhosts 192.157.167.23 192.157.167.21"+'\n'+\
 "In order to know the hosts that have the required ports opened use IPv4_Port_scanner.py or IPv6_Port...\
 This program should support both IPv4 and IPv6. Any suggestions are greatly appriciated. The progrmam must be made executable, and\
 sudo must be used if not root."
	epilog = 'Give me six hours to chop down a tree and I will spend the first four sharpening the axe. Abraham Lincoln'
	parser = argparse.ArgumentParser(usage=usage,epilog=epilog)
	parser.add_argument('-vulnhosts',dest='vh',help ='Hosts on the network that have one of the three optional ports opened : 21,22,23',nargs='+')
	arguments,unknown_args = parser.parse_known_args()
	if unknown_args :
		sys.exit('[!]Unvalid arguments specified: '+str(unknown_args))
	if arguments.vh :
		for host in arguments.vh :
			check_banners(host)

main_arguments()
