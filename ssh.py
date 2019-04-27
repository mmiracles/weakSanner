import paramiko
import threading

class SSHScanner:
    def __init__(self,ip,port=22):
        self.ip = ip
        self.port = port

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
                    info = 'ssh weak password: ip:{}:{},username:{},password:{}\n'.format(self.ip,self.port,username,password)
                    result += info
                    print(info)
        return result

if __name__ == '__main__':
	pass