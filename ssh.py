import paramiko
import threading

# create ssh connection
sshc = paramiko.SSHClient()

# is continue remote connect when first connect,default yes
sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())

class SSHScanner:
	def __init__(self,ip,port=22):
		self.ip = ip
		self.port = port

	def connectSSH(self,username,password):
		try:
			sshc.connect(self.ip,self.port,username,password,timeout=10)
			return 'success'
		except Exception as e:
			if str(e).find("time") >= 0:
				return 'timeout' # 连接超时
			else:
				return 'fail'

if __name__ == '__main__':
	pass