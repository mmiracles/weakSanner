from ftplib import FTP
import argparse
import time

class FTPScanner:
    def __init__(self, ip, port=21,debugLogLevel=1):
        self.ip = ip
        self.port = port
        self.debugLogLevel = debugLogLevel

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
                    info = 'ftp weak password for ip:{}:{},username:{},password:{}'.format(self.ip,self.port,username,password)
                    result += info + '\n'
                    print(info)
                elif self.debugLogLevel >= 2:
                    print('ftp connect {} for ip:{}:{},username:{},password:{}'.format(res,self.ip,self.port,username,password))
        return result

if __name__ == '__main__':
	pass
