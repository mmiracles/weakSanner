from ftplib import FTP
import argparse
import time


class FTPScanner:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port

	def loginAnonymous(self, username, password, timeout=10):
		try:
			with FTP(self.ip) as ftp:
				ftp.login()
				return 'success'
		except Exception as e:
			if "invalid" in str(e) or "failed" in str(e) or 'incorrect' in str(e):
				return 'fail'
			else:
				return 'timeout'

	def login(self, username, password):        # Parameters (hostname, dictionary file)
		try:
			with FTP(self.ip) as ftp:
				ftp.login(username, password)
				return 'success'
		except Exception as e:
			if str(e).find("invalid") > 0 or str(e).find("failed") > 0 or str(e).find("incorrect") > 0:
				return 'fail'
			else:
				return 'timeout'

if __name__ == '__main__':
	pass
    # import xutils
    # host, port = sys.argv[1], int(sys.argv[2])
    # tester = TomcatBruteTester(open('pwd.txt').readlines())
    # rs = tester.test((host,port))
    # print(rs)

        # parser = argparse.ArgumentParser(description='FTP Scanner')
        # parser.add_argument('-H', dest='hostname', help='The host list with ","space')
        # parser.add_argument('-f', dest='pwdFile', help='Password dictionary file')
        # weakScanner = None
        # try:
        # 	weakScanner = parser.parse_args()
        # except:
        # 	print(parser.parse_args(['-h']))
        # 	exit(0)

        # hostNames = str(weakScanner.hostname).split(',')
        # print(weakScanner)
        # pwdFile = weakScanner.pwdFile
        # if hostNames == ['None']:
        # 	print(parser.parse_args(['-h']))
        # 	exit(0)
        # userName = None
        # password = None
        # if anonScan(hostName) == True:
        # 	print('Host: ' + hostName + ' Can anonymously!')
        # else:
        # 	(userName, password) = vlcLogin(hostName, 'pwd.txt')
        # 	print(userName, password)
        # 	if password != None:
        # 		print('\n[+] Host: ' + hostName + 'Username: ' +
        # 				userName + ' Password: ' + password)
        # print('\n[*]-------------------Scan End!--------------------[*]')