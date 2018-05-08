import socket
sniff = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 3)
sniff.bind(("mon0", 0x0003)) # 0x0003 : every packet we get, not like 0x0800 where we get only incoming packets.  
ap_list =[]
while True :
	fm1 = sniff.recvfrom(10000)
	fm= fm1[0]
	if fm[26] == "\x80" : #the first 26 bytes are the radio head part, after that we have the type of the frame\
	#if it == 8 bytes it means it's a beacon frame.
		if fm[36:42] not in ap_list: #36:42 is the BSSID.We append to a the list to prevent redundancy
			ap_list.append(fm[36:42])
			a = ord(fm[63]) #Gives the lenght of the SSID. It is represented as a letter in the unicode. We convert this letter to integer and that's the value of the lenght.
		print "SSID -> ",fm[64:64 +a],"-- BSSID -> ", \
fm[36:42].encode('hex'),"-- Channel -> ", ord(fm[64 +a+12])
#The first char of the SSID is in the 64th position. Which means 
#if we add to this position the lenght of the SSID we get its full
#name. The full lenght  of the SSID + 12 is where the channel is. 
