from scapy.all import * 

eth_p = Ether(dst='84:16:f9:ab:a9:f9 ')
ip_p = IP(src='192.168.178.35',dst='192.168.178.31')
icmp_p = ICMP()
payload = 'l'*1000
packet = (eth_p/ip_p/ICMP()/('x'*60000))
sendp(packet)

#I was not able to send it, because the OS did not let me do it.
#It said the message was too big. 