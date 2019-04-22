import socket
import binascii
import threading
import pymssql


def mysql(ip):
	try:
		with open('user.txt') as userFile:
			for username in userFile.readlines():
				try:
					with open('pwd.txt') as pwdFile:
						for pwd in pwdFile.readlines():
							username = username.replace('\n', '').replace('\r', '')
							pwd = pwd.replace('\n', '').replace('\r', '')
							try:
								conn = pymssql.connect(ip, username, pwd)
								cursor = conn.cursor()
								if not cursor:
									print('失败')
								else:
									print('成功')
								# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
								# s.connect((ip, 1433))
								# print(222)
								# husername = binascii.b2a_hex(username)
								# print(3333)
								# lusername = len(username)
								# lpassword = len(pwd)
								# hpwd = binascii.b2a_hex(pwd)
								# address = binascii.b2a_hex(ip) + '3a' + binascii.b2a_hex(str(1433))
								# data1 = ''.replace(''[16:16+len(address)], address)
								# data2 = data1.replace(data1[78:78+len(husername)], husername)
								# data3 = data2.replace(data2[140:140+len(hpwd)], hpwd)
								# if lusername >= 16:
								# 	data4 = data3.replace('0X', str(hex(lusername)).replace('0x', ''))
								# else:
								# 	data4 = data3.replace('X', str(hex(lusername)).replace('0x', ''))
								# if lpassword >= 16:
								# 	data5 = data4.replace('0Y', str(hex(lpassword)).replace('0x', ''))
								# else:
								# 	data5 = data4.replace('Y', str(hex(lpassword)).replace('0x', ''))
								# hladd = hex(len(ip) + len(str(1433))+1).replace('0x', '')
								# data6 = data5.replace('ZZ', str(hladd))
								# data7 = binascii.a2b_hex(data6)
								# s.send(data7)
								# if 'master' in s.recv(1024):
								# 	print(u'[+] {}:1433  SQLserver存在弱口令: sa  {}'.format(ip, pwd))
								# else:
								# 	print(s.recv(1024))
							except Exception as e:
								if(str(e).find('18456')==-1):
									print(e)
									return
								pass
							# finally:
							# 	s.close()
				except:
					pass
	except:
		pass


def main():
	for ip3 in range(1,2):
		for ip4 in range(1,255):
			threading.Thread(target=mysql,args=('192.168.'+str(ip3)+'.' + str(ip4),)).start()


if __name__ == '__main__':
    main()
