import paramiko
import threading
import time

class SSHScanner:
    def __init__(self,ip,port=22,debugLogLevel=1):
        self.ip = ip
        self.port = port
        self.debugLogLevel = debugLogLevel

    def connectSSH(self,username,password):
        try:
            # create ssh connection
            sshc = paramiko.SSHClient()
            sshc.banner_timeout = 300
            # is continue remote connect when first connect,default yes
            sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sshc.connect(self.ip,self.port,username,password,timeout=10)
            return 'success'
        except Exception as e:
            if str(e).find("time") >= 0:
                return 'timeout' 
            else:
                return 'fail'
                
    def scanWeakPwsd(self, pwdLines):  
        result = ''
        for username in pwdLines:
            for password in pwdLines:
                username = username.strip('\r').strip('\n')
                password = password.strip('\r').strip('\n')
                res = self.connectSSH(username, password)
                if res == 'success':
                    info = 'ssh weak password for ip:{}:{},username:{},password:{}'.format(self.ip,self.port,username,password)
                    result += info +'\n'
                    print(info)
                elif self.debugLogLevel >= 2:
                    print('ssh connect {} for ip:{}:{},username:{},password:{}'.format(res,self.ip,self.port,username,password))
                time.sleep(0.5)
        return result

if __name__ == '__main__':
	pass