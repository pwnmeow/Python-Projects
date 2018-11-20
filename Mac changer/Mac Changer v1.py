#!/usr/bin/env/ python
import subprocess
import optparse

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface",dest="interface",help="interface to change its MAC address")
	parser.add_option("-m", "--mac",dest="new_MAC",help="New Mac address")
	(options,arguments) = parser.parse_args()
	if not options.interface:
		#code to handle errors
		parser.error("[-] Please specify an interface use --help for more info.")
	elif not options.new_MAC:
		#code to handle errors
		parser.error("[-] Please specify an mac use --help for more info.")
	return options

def change_mac(interface,new_mac):
	print("[+] Changeing MAC address for "+ interface + " to "+ new_mac)
	subprocess.call(["ifconfig" , interface , "down"])
	subprocess.call(["ifconfig" , interface , "hw","ether",new_mac])
	subprocess.call(["ifconfig" , interface , "up"])

# option parser is a class
options = get_args() 
change_mac(options.interface,options.new_MAC)

# v2 no secureity implemented you can execute commands 
# subprocess.call("ifconfig " + interface +" down" ,shell=True)
# subprocess.call("ifconfig "+ interface +" hw ether "+ new_MAC ,shell=True)
# subprocess.call("ifconfig "+ interface +" up",shell=True)


# v1
# subprocess.call("ifconfig wlan0 down",shell=True)
# subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55:66",shell=True)
# subprocess.call("ifconfig wlan0 up",shell=True)