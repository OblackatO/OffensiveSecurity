import socket, binascii, struct 

#----------------------General Part----------------------------#
s_i = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0800))
#s_i = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0003))

while True:
	packet_i = s_i.recvfrom(2048)
	print('\n'+'@@@@@@@@@@ EtherNet Frame @@@@@@@@@@')
	eth_p = packet_i[0][0:14]
	unpack_eth_p = struct.unpack('!6s6s2s',eth_p)
	dest_mac = unpack_eth_p[0]
	sour_mac = unpack_eth_p[1]
	print('[>]Source MAC address :',binascii.hexlify(sour_mac).decode(),'\n'+
		  '[>]Destination MAC address :',binascii.hexlify(dest_mac).decode())
	print('@@@@@@@@@@ Internal Protocol @@@@@@@@@@')
	ip_p = packet_i[0][14:34] #See note (1)
	unpack_ip_p = struct.unpack('!8sB3s4s4s',ip_p)
	sourc_ip = socket.inet_ntoa(unpack_ip_p[3])
	dest_ip = socket.inet_ntoa(unpack_ip_p[4])
	ttl_ip = unpack_ip_p[1]
	print('[>]Source IP :',sourc_ip+'\n'+
		  '[>]Destination IP :',dest_ip+'\n'+
		  '[>]TTL :',ttl_ip)
	print('@@@@@@@@@@ Transport Layer Protocol @@@@@@@@@@')
	trans_p = packet_i[0][34:54] #See note (1)
	#unpack_trans_p = struct.unpack('!HH16s',trans_p) #See note (2)
	unpack_trans_p = struct.unpack('!HH9ss6s',trans_p) #IF FLAG WANTED : IT IS IN THE 10TH POSITION, THE s. 
	print('[>]Source Port :',unpack_trans_p[0],'\n'+
		  '[>]Destination Port :',unpack_trans_p[1],'\n'+
		  '[>]Flag :', binascii.hexlify(unpack_trans_p[3]).decode())

	#I stopped here


"""
Note (1) : 

The IP layer and transport layer have both additional arguments 
which can be added in their header. If these arguments are added
the header will be longer than 20 bytes, and because of this 
the number we use to get each layer out og packet_i[0] could 
not work. 

Note (2) : 

The flag will not be extracted. 
"""