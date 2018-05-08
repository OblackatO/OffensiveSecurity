import socket

s_i = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0003))
s_i.bind(('wlan0mon',0x0003))
bssid_list = []
while True:
	rev_data = s_i.recvfrom(6000)
	rev_data1 = rev_data[0]
	if rev_data1[26] == '\x08' : 
		bssid_i = rev_data1[36:42].encode('hex')
		if bssid_i in bssid_list :
			pass
		else:
			bssid_list.append(bssid_i)
			ssid_lenght = ord(rev_data1[63])
			ssid_i = rev_data1[64:64 + ssid_lenght]
			channel = ord(rev_data1[64 + ssid_lenght + 12 ])
			print('[>]Beacon Frame found, SSID:',ssid_i,'BSSID:',bssid_i\
				   ,'Channel:',channel)
	else:
		pass

#This script did not work, the one made with scapy worked fine.
#See scapy folder, script beacon_scapy.py for more details. 