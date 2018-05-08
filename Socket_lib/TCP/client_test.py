import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('IP Adress',port))
message_to_sever = 'Hello server'
client_socket.send(message_to_sever.encode())
#buf = bytearray("-" * 25,'utf-8') #1
#message_from_server = client_socket.recv_into(buf,25)#1
message_from_server, addr = client_socket.recvfrom(1024)
print('[>]Message from server:',message_from_server.decode())
#print('[>]Message from server:',buf.decode(),'Bytes:',message_from_server) #1
client_socket.close()


"""
#1  The function recv_into(buf,25) will save the message into a buffer defined by the user
using the bytearray function. We set the maximum size of the buffer, in this case 25
and we also set the maximum size of the recv message from the client/server in the 
recv_into function. If the receive message is less than the defined size, the rest of
the buffer will be fullfielded with the characters used to fill the bytearray. 
An error will occur if the message is bigger than the defined size. 

"""
