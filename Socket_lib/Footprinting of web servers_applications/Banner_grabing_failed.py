import socket

s1 = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0800))
while True :
	data = s1.recvfrom(2048)
	banner = data[0][54:545]
	print('-'*50)

"""
import socket 

#Can be adapted to ipv6 if needed

target = input('[>]Enter the url:')
target = socket.gethostbyname(target)

s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect((target,80))
#s1.send('Grabing banner'.encode())
banner = s1.recv(1024)
print(banner.decode())

I was not able to get the banner with both of the previous codes. I tried
different websites without sucess. I think banner grabbing is almost
the same thing as the information the headers provide.
"""