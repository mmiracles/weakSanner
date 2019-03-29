import telnetlib;
import time;
import threading;
22222222
def connectTelnet(username):
	tn = telnetlib.Telnet("192.168.1.101",timeout=5);
	tn.set_debuglevel(0);
	print(username)
	tn.read_until(b"Login username:");
	print("logining");
	tn.write(username);
	tn.write(b"8001715057\r\n");
	tn.write(b"\r\n");
	print(tn.read_until(b'Domain name:'));
	'''
	result = tn.read_some();
	try:
		result = result + tn.read_some();
		result = result + tn.read_some();
	
	except Exception as e:
		pass;
	print(result)
	'''
	
	res = tn.read_until(b'failed',timeout=5);
	
	if res.find(b'failed') > 0:
		print("login failed");
	else:
		print("login success");
	tn.close();

file = open(b"pwd.txt");	
while 1:
	fileText = file.readline();
	print(fileText)
	connectTelnet(b"aaa");
	time.sleep(0.02);
