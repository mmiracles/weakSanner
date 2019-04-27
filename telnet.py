import telnetlib
import time
import threading


class TelnetScanner:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connectTelnet(self, user, pwd):
        try:
            user = user.encode()
            pwd = pwd.encode()
            tn = telnetlib.Telnet(self.ip, timeout=20)
            tn.set_debuglevel(0)
            a = tn.expect([b"login", b"Login", b"name"], timeout=10)
            tn.write(user+b"\r\n")
            tn.expect([b"word"], timeout=20)
            tn.write(pwd+b"\r\n")
            tn.write(b"\r\n")
            res = tn.expect([b'Failed', b'failed', b'invalid',
                             b'incorrect'], timeout=10)
            if res[0] >= 0:
                return 'fail'
            else:
                return 'success'
            tn.close()
        except Exception as e:
            return 'timeout'

    def scanWeakPwsd(self, pwdLines):
        result = ''
        for username in pwdLines:
            for password in pwdLines:
                username = username.strip('\r').strip('\n')
                password = password.strip('\r').strip('\n')
                res = self.connectTelnet(username, password)
                if res == 'success':
                    info = 'telnet weak password: ip:{}:{},username:{},password:{}\n'.format(
                        self.ip, self.port, username, password)
                    result += info
                    print(info)
        return result


'''
for ip1 in range(202,203):
	for ip2 in range(3,4):
		for ip3 in range(29,30):
			for ip4 in range(1,2):
				t=threading.Thread(target=dfs,name='runThread',args=(str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4),))
				t.start()
'''
# t=threading.Thread(target=dfs,name='runThread',args=('129.204.234.135',))
# t.start()
