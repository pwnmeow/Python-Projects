#!/usr/bin/env/ python
import subprocess
import optparse
import re

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

def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig",interface]).decode('utf-8')
	mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
	if mac_search_result:
		return mac_search_result.group(0)
	else:
		print("[-] Sorry could not read MAC address.")
#Gets args from commandline 
options = get_args() 
current_mac = get_current_mac(options.interface)
print("[-] Current Mac: "+ str(current_mac))

change_mac(options.interface,options.new_MAC)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_MAC:
	print("[+] MAC address was succesfuly changed to "+ options.new_MAC)
else:
	print("[-] MAC address couldnt be changed")
	print("[-] According to standerds MAC should start with and even pair")

# v2 no secureity implemented you can execute commands 
# subprocess.call("ifconfig " + interface +" down" ,shell=True)
# subprocess.call("ifconfig "+ interface +" hw ether "+ new_MAC ,shell=True)
# subprocess.call("ifconfig "+ interface +" up",shell=True)


# v1
# subprocess.call("ifconfig wlan0 down",shell=True)
# subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55:66",shell=True)
# subprocess.call("ifconfig wlan0 up",shell=True)