#!/usr/bin/env python
import scapy.all as scapy 
print("Help:- just run and enter  ip's or range of ips as [10.0.3.1/24] ")
ip_add = input("[-] Enter ip address : ")
def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  
	arp_request_broadcast = broadcast/arp_request 
	answerd_list = scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0] # v2
	client_list = []
	for element in answerd_list: #NOTE 3
		client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
		client_list.append(client_dict)
	return client_list

def print_results(result_list):
	print("IP\t\t\tMAC Address\n----------------------------------------------------------")
	for client in result_list:
		print(client["ip"] + "\t\t" + client["mac"])

scan_result =scan(ip_add)
print_results(scan_result) 
#+===============================================REFACTOR=================================================================================

# #!/usr/bin/env python
# import scapy.all as scapy #library to make packets and work with arp

# def scan(ip):
# 	arp_request = scapy.ARP(pdst=ip) # Initiateing scapy as a call and loading arp object from it 
# 	# scapy.ls(scapy.ARP()) // gives options to set for arp packet
# 	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # sets the mac of packet to broad cast ff*6 times is broadcast mac
# 	# scapy.ls(scapy.Ether()) // this returns options we can set in ether object
# 	arp_request_broadcast = broadcast/arp_request # "/" joins to packets  together
# 	# print(arp_request_broadcast.summary()) // this shows summary
# 	# arp_request_broadcast.show() // this shows full details of a packet
# 	#====================SRP=========================================================================================
# 	answerd_list = scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0] # v2

# 	print("IP\t\t\tMac Address\n-------------------------------------------------")
# 	for element in answerd_list: #NOTE 3
# 		print(element[1].psrc +"\t\t" + element[1].hwsrc) # to get the ip of the client who responded to us see to see what show sentNote:4
# 		# to get the clients mac who responded to us  Note:4 
# 		#	print(element[1].show())  Note 4 to see ip address and mac of the cliednt who responded
# 		# print("-----------------------------------------------------------------")
# 	# answerd_list,unanswerd_list = scapy.srp(arp_request_broadcast, timeout=1) # sends the packet and recives a response,
# 	# Takes 2 parameters for answerd responses and non answerd responses 
# 	# second parameter is timeout to time out if do not get response after  one second
# 	#	print(answerd_list.summary())# answerd responses ++++++++++++++++++++++++++++++++++++++++++++>:NOTE 1
# 	#	print(unanswerd_list.summary()) unanswerd responses +++++++++++++++++++++++++++++++++++++++++>:NOTE 2
# 	#================================================================================================================

# 	# PRINTING THE RESULT IN TABLE



# scan("10.0.9.1/24") #CALLING THE SCAN CUSTOM FUNCTION MENTIONED ABOVE
#+===============================================REFACTOR==================================================================





#======================================================================================================================
															#NOTE's
#======================================================================================================================

#NOTE:1

# └──╼ #python3 pract.py 
# Begin emission:
# ***Finished sending 256 packets.
# *
# Received 4 packets, got 4 answers, remaining 252 packets
# Ether / ARP who has 10.0.9.1 says 10.0.9.131 ==> Ether / ARP is at 00:50:56:c0:00:00 says 10.0.9.1 / Padding
# Ether / ARP who has 10.0.9.2 says 10.0.9.131 ==> Ether / ARP is at 00:50:56:e5:c6:95 says 10.0.9.2 / Padding
# Ether / ARP who has 10.0.9.136 says 10.0.9.131 ==> Ether / ARP is at 00:0c:29:04:9d:fa says 10.0.9.136 / Padding
# Ether / ARP who has 10.0.9.254 says 10.0.9.131 ==> Ether / ARP is at 00:50:56:e3:1e:4c says 10.0.9.254 / Padding
# None

#===========================================================================================================================
#NOTE:3

# ┌─[root@parrot]─[/home/batcave/Desktop]
# └──╼ #python3 pract.py 
# Begin emission:
# ***Finished sending 256 packets.
# *
# Received 4 packets, got 4 answers, remaining 252 packets
# (<Ether  dst=ff:ff:ff:ff:ff:ff type=0x806 |<ARP  pdst=10.0.9.2 |>>, <Ether  dst=00:0c:29:e1:80:57 src=00:50:56:e5:c6:95 type=0x806 |<ARP  hwtype=0x1 ptype=0x800 hwlen=6 plen=4 op=is-at hwsrc=00:50:56:e5:c6:95 psrc=10.0.9.2 hwdst=00:0c:29:e1:80:57 pdst=10.0.9.131 |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>)
# -----------------------------------------------------------------
#===========================================================================================================================
# NOTE:4


# ##[ Ethernet ]### 
#   dst       = 00:0c:29:e1:80:57
#   src       = 00:50:56:e3:1e:4c
#   type      = 0x806
# ###[ ARP ]### 
#      hwtype    = 0x1
#      ptype     = 0x800
#      hwlen     = 6
#      plen      = 4
#      op        = is-at
#      hwsrc     = 00:50:56:e3:1e:4c
#      psrc      = 10.0.9.254
#      hwdst     = 00:0c:29:e1:80:57
#      pdst      = 10.0.9.131
# ###[ Padding ]### 
#         load      = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# None
# -----------------------------------------------------------------
#===========================================================================================================================

#===========================================================================================================================

#NOTE:2

# └──╼ #python3 pract.py 
# Begin emission:
# ***Finished sending 256 packets.
# *
# Received 4 packets, got 4 answers, remaining 252 packets
# Ether / ARP who has 10.0.9.0 says 10.0.9.131
# Ether / ARP who has 10.0.9.3 says 10.0.9.131
# Ether / ARP who has 10.0.9.4 says 10.0.9.131
# Ether / ARP who has 10.0.9.5 says 10.0.9.131
# Ether / ARP who has 10.0.9.6 says 10.0.9.131
# Ether / ARP who has 10.0.9.7 says 10.0.9.131
# Ether / ARP who has 10.0.9.8 says 10.0.9.131
# Ether / ARP who has 10.0.9.9 says 10.0.9.131
# Ether / ARP who has 10.0.9.10 says 10.0.9.131
# Ether / ARP who has 10.0.9.11 says 10.0.9.131
# Ether / ARP who has 10.0.9.12 says 10.0.9.131
# Ether / ARP who has 10.0.9.13 says 10.0.9.131
# Ether / ARP who has 10.0.9.14 says 10.0.9.131
# Ether / ARP who has 10.0.9.15 says 10.0.9.131
# Ether / ARP who has 10.0.9.16 says 10.0.9.131
# Ether / ARP who has 10.0.9.17 says 10.0.9.131
# Ether / ARP who has 10.0.9.18 says 10.0.9.131
# Ether / ARP who has 10.0.9.19 says 10.0.9.131
# Ether / ARP who has 10.0.9.20 says 10.0.9.131
# Ether / ARP who has 10.0.9.21 says 10.0.9.131
# Ether / ARP who has 10.0.9.22 says 10.0.9.131
# Ether / ARP who has 10.0.9.23 says 10.0.9.131
# Ether / ARP who has 10.0.9.24 says 10.0.9.131
# Ether / ARP who has 10.0.9.25 says 10.0.9.131
# Ether / ARP who has 10.0.9.26 says 10.0.9.131
# Ether / ARP who has 10.0.9.27 says 10.0.9.131
# Ether / ARP who has 10.0.9.28 says 10.0.9.131
# Ether / ARP who has 10.0.9.29 says 10.0.9.131
# Ether / ARP who has 10.0.9.30 says 10.0.9.131
# Ether / ARP who has 10.0.9.31 says 10.0.9.131
# Ether / ARP who has 10.0.9.32 says 10.0.9.131
# Ether / ARP who has 10.0.9.33 says 10.0.9.131
# Ether / ARP who has 10.0.9.34 says 10.0.9.131
# Ether / ARP who has 10.0.9.35 says 10.0.9.131
# Ether / ARP who has 10.0.9.36 says 10.0.9.131
# Ether / ARP who has 10.0.9.37 says 10.0.9.131
# Ether / ARP who has 10.0.9.38 says 10.0.9.131
# Ether / ARP who has 10.0.9.39 says 10.0.9.131
# Ether / ARP who has 10.0.9.40 says 10.0.9.131
# Ether / ARP who has 10.0.9.41 says 10.0.9.131
# Ether / ARP who has 10.0.9.42 says 10.0.9.131
# Ether / ARP who has 10.0.9.43 says 10.0.9.131
# Ether / ARP who has 10.0.9.44 says 10.0.9.131
# Ether / ARP who has 10.0.9.45 says 10.0.9.131
# Ether / ARP who has 10.0.9.46 says 10.0.9.131
# Ether / ARP who has 10.0.9.47 says 10.0.9.131
# Ether / ARP who has 10.0.9.48 says 10.0.9.131
# Ether / ARP who has 10.0.9.49 says 10.0.9.131
# Ether / ARP who has 10.0.9.50 says 10.0.9.131
# Ether / ARP who has 10.0.9.51 says 10.0.9.131
# Ether / ARP who has 10.0.9.52 says 10.0.9.131
# Ether / ARP who has 10.0.9.53 says 10.0.9.131
# Ether / ARP who has 10.0.9.54 says 10.0.9.131
# Ether / ARP who has 10.0.9.55 says 10.0.9.131
# Ether / ARP who has 10.0.9.56 says 10.0.9.131
# Ether / ARP who has 10.0.9.57 says 10.0.9.131
# Ether / ARP who has 10.0.9.58 says 10.0.9.131
# Ether / ARP who has 10.0.9.59 says 10.0.9.131
# Ether / ARP who has 10.0.9.60 says 10.0.9.131
# Ether / ARP who has 10.0.9.61 says 10.0.9.131
# Ether / ARP who has 10.0.9.62 says 10.0.9.131
# Ether / ARP who has 10.0.9.63 says 10.0.9.131
# Ether / ARP who has 10.0.9.64 says 10.0.9.131
# Ether / ARP who has 10.0.9.65 says 10.0.9.131
# Ether / ARP who has 10.0.9.66 says 10.0.9.131
# Ether / ARP who has 10.0.9.67 says 10.0.9.131
# Ether / ARP who has 10.0.9.68 says 10.0.9.131
# Ether / ARP who has 10.0.9.69 says 10.0.9.131
# Ether / ARP who has 10.0.9.70 says 10.0.9.131
# Ether / ARP who has 10.0.9.71 says 10.0.9.131
# Ether / ARP who has 10.0.9.72 says 10.0.9.131
# Ether / ARP who has 10.0.9.73 says 10.0.9.131
# Ether / ARP who has 10.0.9.74 says 10.0.9.131
# Ether / ARP who has 10.0.9.75 says 10.0.9.131
# Ether / ARP who has 10.0.9.76 says 10.0.9.131
# Ether / ARP who has 10.0.9.77 says 10.0.9.131
# Ether / ARP who has 10.0.9.78 says 10.0.9.131
# Ether / ARP who has 10.0.9.79 says 10.0.9.131
# Ether / ARP who has 10.0.9.80 says 10.0.9.131
# Ether / ARP who has 10.0.9.81 says 10.0.9.131
# Ether / ARP who has 10.0.9.82 says 10.0.9.131
# Ether / ARP who has 10.0.9.83 says 10.0.9.131
# Ether / ARP who has 10.0.9.84 says 10.0.9.131
# Ether / ARP who has 10.0.9.85 says 10.0.9.131
# Ether / ARP who has 10.0.9.86 says 10.0.9.131
# Ether / ARP who has 10.0.9.87 says 10.0.9.131
# Ether / ARP who has 10.0.9.88 says 10.0.9.131
# Ether / ARP who has 10.0.9.89 says 10.0.9.131
# Ether / ARP who has 10.0.9.90 says 10.0.9.131
# Ether / ARP who has 10.0.9.91 says 10.0.9.131
# Ether / ARP who has 10.0.9.92 says 10.0.9.131
# Ether / ARP who has 10.0.9.93 says 10.0.9.131
# Ether / ARP who has 10.0.9.94 says 10.0.9.131
# Ether / ARP who has 10.0.9.95 says 10.0.9.131
# Ether / ARP who has 10.0.9.96 says 10.0.9.131
# Ether / ARP who has 10.0.9.97 says 10.0.9.131
# Ether / ARP who has 10.0.9.98 says 10.0.9.131
# Ether / ARP who has 10.0.9.99 says 10.0.9.131
# Ether / ARP who has 10.0.9.100 says 10.0.9.131
# Ether / ARP who has 10.0.9.101 says 10.0.9.131
# Ether / ARP who has 10.0.9.102 says 10.0.9.131
# Ether / ARP who has 10.0.9.103 says 10.0.9.131
# Ether / ARP who has 10.0.9.104 says 10.0.9.131
# Ether / ARP who has 10.0.9.105 says 10.0.9.131
# Ether / ARP who has 10.0.9.106 says 10.0.9.131
# Ether / ARP who has 10.0.9.107 says 10.0.9.131
# Ether / ARP who has 10.0.9.108 says 10.0.9.131
# Ether / ARP who has 10.0.9.109 says 10.0.9.131
# Ether / ARP who has 10.0.9.110 says 10.0.9.131
# Ether / ARP who has 10.0.9.111 says 10.0.9.131
# Ether / ARP who has 10.0.9.112 says 10.0.9.131
# Ether / ARP who has 10.0.9.113 says 10.0.9.131
# Ether / ARP who has 10.0.9.114 says 10.0.9.131
# Ether / ARP who has 10.0.9.115 says 10.0.9.131
# Ether / ARP who has 10.0.9.116 says 10.0.9.131
# Ether / ARP who has 10.0.9.117 says 10.0.9.131
# Ether / ARP who has 10.0.9.118 says 10.0.9.131
# Ether / ARP who has 10.0.9.119 says 10.0.9.131
# Ether / ARP who has 10.0.9.120 says 10.0.9.131
# Ether / ARP who has 10.0.9.121 says 10.0.9.131
# Ether / ARP who has 10.0.9.122 says 10.0.9.131
# Ether / ARP who has 10.0.9.123 says 10.0.9.131
# Ether / ARP who has 10.0.9.124 says 10.0.9.131
# Ether / ARP who has 10.0.9.125 says 10.0.9.131
# Ether / ARP who has 10.0.9.126 says 10.0.9.131
# Ether / ARP who has 10.0.9.127 says 10.0.9.131
# Ether / ARP who has 10.0.9.128 says 10.0.9.131
# Ether / ARP who has 10.0.9.129 says 10.0.9.131
# Ether / ARP who has 10.0.9.130 says 10.0.9.131
# Ether / ARP who has 10.0.9.131 says 10.0.9.131
# Ether / ARP who has 10.0.9.132 says 10.0.9.131
# Ether / ARP who has 10.0.9.133 says 10.0.9.131
# Ether / ARP who has 10.0.9.134 says 10.0.9.131
# Ether / ARP who has 10.0.9.135 says 10.0.9.131
# Ether / ARP who has 10.0.9.137 says 10.0.9.131
# Ether / ARP who has 10.0.9.138 says 10.0.9.131
# Ether / ARP who has 10.0.9.139 says 10.0.9.131
# Ether / ARP who has 10.0.9.140 says 10.0.9.131
# Ether / ARP who has 10.0.9.141 says 10.0.9.131
# Ether / ARP who has 10.0.9.142 says 10.0.9.131
# Ether / ARP who has 10.0.9.143 says 10.0.9.131
# Ether / ARP who has 10.0.9.144 says 10.0.9.131
# Ether / ARP who has 10.0.9.145 says 10.0.9.131
# Ether / ARP who has 10.0.9.146 says 10.0.9.131
# Ether / ARP who has 10.0.9.147 says 10.0.9.131
# Ether / ARP who has 10.0.9.148 says 10.0.9.131
# Ether / ARP who has 10.0.9.149 says 10.0.9.131
# Ether / ARP who has 10.0.9.150 says 10.0.9.131
# Ether / ARP who has 10.0.9.151 says 10.0.9.131
# Ether / ARP who has 10.0.9.152 says 10.0.9.131
# Ether / ARP who has 10.0.9.153 says 10.0.9.131
# Ether / ARP who has 10.0.9.154 says 10.0.9.131
# Ether / ARP who has 10.0.9.155 says 10.0.9.131
# Ether / ARP who has 10.0.9.156 says 10.0.9.131
# Ether / ARP who has 10.0.9.157 says 10.0.9.131
# Ether / ARP who has 10.0.9.158 says 10.0.9.131
# Ether / ARP who has 10.0.9.159 says 10.0.9.131
# Ether / ARP who has 10.0.9.160 says 10.0.9.131
# Ether / ARP who has 10.0.9.161 says 10.0.9.131
# Ether / ARP who has 10.0.9.162 says 10.0.9.131
# Ether / ARP who has 10.0.9.163 says 10.0.9.131
# Ether / ARP who has 10.0.9.164 says 10.0.9.131
# Ether / ARP who has 10.0.9.165 says 10.0.9.131
# Ether / ARP who has 10.0.9.166 says 10.0.9.131
# Ether / ARP who has 10.0.9.167 says 10.0.9.131
# Ether / ARP who has 10.0.9.168 says 10.0.9.131
# Ether / ARP who has 10.0.9.169 says 10.0.9.131
# Ether / ARP who has 10.0.9.170 says 10.0.9.131
# Ether / ARP who has 10.0.9.171 says 10.0.9.131
# Ether / ARP who has 10.0.9.172 says 10.0.9.131
# Ether / ARP who has 10.0.9.173 says 10.0.9.131
# Ether / ARP who has 10.0.9.174 says 10.0.9.131
# Ether / ARP who has 10.0.9.175 says 10.0.9.131
# Ether / ARP who has 10.0.9.176 says 10.0.9.131
# Ether / ARP who has 10.0.9.177 says 10.0.9.131
# Ether / ARP who has 10.0.9.178 says 10.0.9.131
# Ether / ARP who has 10.0.9.179 says 10.0.9.131
# Ether / ARP who has 10.0.9.180 says 10.0.9.131
# Ether / ARP who has 10.0.9.181 says 10.0.9.131
# Ether / ARP who has 10.0.9.182 says 10.0.9.131
# Ether / ARP who has 10.0.9.183 says 10.0.9.131
# Ether / ARP who has 10.0.9.184 says 10.0.9.131
# Ether / ARP who has 10.0.9.185 says 10.0.9.131
# Ether / ARP who has 10.0.9.186 says 10.0.9.131
# Ether / ARP who has 10.0.9.187 says 10.0.9.131
# Ether / ARP who has 10.0.9.188 says 10.0.9.131
# Ether / ARP who has 10.0.9.189 says 10.0.9.131
# Ether / ARP who has 10.0.9.190 says 10.0.9.131
# Ether / ARP who has 10.0.9.191 says 10.0.9.131
# Ether / ARP who has 10.0.9.192 says 10.0.9.131
# Ether / ARP who has 10.0.9.193 says 10.0.9.131
# Ether / ARP who has 10.0.9.194 says 10.0.9.131
# Ether / ARP who has 10.0.9.195 says 10.0.9.131
# Ether / ARP who has 10.0.9.196 says 10.0.9.131
# Ether / ARP who has 10.0.9.197 says 10.0.9.131
# Ether / ARP who has 10.0.9.198 says 10.0.9.131
# Ether / ARP who has 10.0.9.199 says 10.0.9.131
# Ether / ARP who has 10.0.9.200 says 10.0.9.131
# Ether / ARP who has 10.0.9.201 says 10.0.9.131
# Ether / ARP who has 10.0.9.202 says 10.0.9.131
# Ether / ARP who has 10.0.9.203 says 10.0.9.131
# Ether / ARP who has 10.0.9.204 says 10.0.9.131
# Ether / ARP who has 10.0.9.205 says 10.0.9.131
# Ether / ARP who has 10.0.9.206 says 10.0.9.131
# Ether / ARP who has 10.0.9.207 says 10.0.9.131
# Ether / ARP who has 10.0.9.208 says 10.0.9.131
# Ether / ARP who has 10.0.9.209 says 10.0.9.131
# Ether / ARP who has 10.0.9.210 says 10.0.9.131
# Ether / ARP who has 10.0.9.211 says 10.0.9.131
# Ether / ARP who has 10.0.9.212 says 10.0.9.131
# Ether / ARP who has 10.0.9.213 says 10.0.9.131
# Ether / ARP who has 10.0.9.214 says 10.0.9.131
# Ether / ARP who has 10.0.9.215 says 10.0.9.131
# Ether / ARP who has 10.0.9.216 says 10.0.9.131
# Ether / ARP who has 10.0.9.217 says 10.0.9.131
# Ether / ARP who has 10.0.9.218 says 10.0.9.131
# Ether / ARP who has 10.0.9.219 says 10.0.9.131
# Ether / ARP who has 10.0.9.220 says 10.0.9.131
# Ether / ARP who has 10.0.9.221 says 10.0.9.131
# Ether / ARP who has 10.0.9.222 says 10.0.9.131
# Ether / ARP who has 10.0.9.223 says 10.0.9.131
# Ether / ARP who has 10.0.9.224 says 10.0.9.131
# Ether / ARP who has 10.0.9.225 says 10.0.9.131
# Ether / ARP who has 10.0.9.226 says 10.0.9.131
# Ether / ARP who has 10.0.9.227 says 10.0.9.131
# Ether / ARP who has 10.0.9.228 says 10.0.9.131
# Ether / ARP who has 10.0.9.229 says 10.0.9.131
# Ether / ARP who has 10.0.9.230 says 10.0.9.131
# Ether / ARP who has 10.0.9.231 says 10.0.9.131
# Ether / ARP who has 10.0.9.232 says 10.0.9.131
# Ether / ARP who has 10.0.9.233 says 10.0.9.131
# Ether / ARP who has 10.0.9.234 says 10.0.9.131
# Ether / ARP who has 10.0.9.235 says 10.0.9.131
# Ether / ARP who has 10.0.9.236 says 10.0.9.131
# Ether / ARP who has 10.0.9.237 says 10.0.9.131
# Ether / ARP who has 10.0.9.238 says 10.0.9.131
# Ether / ARP who has 10.0.9.239 says 10.0.9.131
# Ether / ARP who has 10.0.9.240 says 10.0.9.131
# Ether / ARP who has 10.0.9.241 says 10.0.9.131
# Ether / ARP who has 10.0.9.242 says 10.0.9.131
# Ether / ARP who has 10.0.9.243 says 10.0.9.131
# Ether / ARP who has 10.0.9.244 says 10.0.9.131
# Ether / ARP who has 10.0.9.245 says 10.0.9.131
# Ether / ARP who has 10.0.9.246 says 10.0.9.131
# Ether / ARP who has 10.0.9.247 says 10.0.9.131
# Ether / ARP who has 10.0.9.248 says 10.0.9.131
# Ether / ARP who has 10.0.9.249 says 10.0.9.131
# Ether / ARP who has 10.0.9.250 says 10.0.9.131
# Ether / ARP who has 10.0.9.251 says 10.0.9.131
# Ether / ARP who has 10.0.9.252 says 10.0.9.131
# Ether / ARP who has 10.0.9.253 says 10.0.9.131
# Ether / ARP who has 10.0.9.255 says 10.0.9.131
# None
