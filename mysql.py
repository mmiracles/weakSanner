import pymysql
import threading

class MysqlScanner:
	def __init__(self,ip,port=3306):
		self.ip = ip
		self.port = port

	def connect(self,username,password):
		try:
			conn = pymysql.connect(self.ip ,username, password, 'mysql',self.port)
			conn.close()
			return 'success'
		except Exception as e:
			if(str(e).find('1045')==-1):
				# print(e)
				return 'timeout'
			else:
				return 'fail'

if __name__ == '__main__':
	for ip3 in range(234,235):
		for ip4 in range(0,255):
			threading.Thread(target=MysqlScanner('129.204.234.135').connect,args=('129.204.'+str(ip3)+'.' + str(ip4),)).start()