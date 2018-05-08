import socket

client_side = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
message = 'Hello server'
client_side.sendto(message.encode(),("::1",54321))
message,addr = client_side.recvfrom(30)
print('[>]Message from server:',message.decode())
client_side.close()