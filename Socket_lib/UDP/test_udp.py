import socket 

host = "::1"
port = 54321
#getaddrinfo resturns 5 tuple : (family, type, proto, canonname, sockaddr)
for item in socket.getaddrinfo(host,port,family=socket.AF_INET6,type=socket.SOCK_DGRAM) :
	family,type1,proto,can,sockaddr = item 
	try:
		server_side = socket.socket(family,type1,proto)
	except OSError as e : 
		server_side = None
		continue
server_side.bind(sockaddr)
server_side.settimeout(10)
while True:
	try:
		message,addr = server_side.recvfrom(100)
		print('[>]Client message:',message.decode(),'--Client address:',addr[0])
		server_side.sendto('Welcome to the server client !'.encode(),(addr[0],addr[1]))
		server_side.close()
	except (socket.herror,socket.timeout,socket.gaierror,socket.error) as e :
		if 'socket.herror' in str(e): 
			print('[!]Adress related error.')
			server_side.close()
		if 'socket.timeout' in str(e): 
			print('[!]Server timed out.')
			server_side.close()
		if 'socket.gaierror' in str(e): 
			print('[!]Error getting address aditional information.')
			server_side.close()
		if 'socket.error' in str(e): 
			print('[!]An error occured.')
			server_side.close()

""" 
Creating UDP server with IPv6 : 

Building IPv6 sockets requires more than just the host name and its port. We need to
specify the family and the type of the socket with the getaddrinfo function. 
This function will return a 5 elements tuple (family, type, proto, canonname, sockaddr)
the family,type and proto arguments can be used in the socket() function to create 
tje socket, finally the sockaddr argument, which is a four element tuple for IPv6
and two element tuple for IPv4 can be used in the bind() function. 

I noticed that the server was not able to receive more than one request after I started it,
but it could also be a problem on the client side. 