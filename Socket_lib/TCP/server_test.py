import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('192.168.178.87',54321))
server_socket.listen(1)
while True : #Infinite loop to accept connection without turning off the server.
	connection, addr_connecting = server_socket.accept()
	message_from_client,addr = connection.recvfrom(1024)
	print('[>]Connection from:',addr_connecting)
	print('[>]Message from client:', message_from_client.decode())
	message_to_client = 'Welcome to the server ! '
	connection.send(message_to_client.encode())
	connection.close()

"""
#we will make a server-side program that offers a connection to the client and
#sends a message to the client. Run server1.py :
"""

