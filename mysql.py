import pymysql;

def mysql(ip):
		for pwd in range(0,1):
			try:
				pwd = 'ldj_group_buying';
				conn = pymysql.connect(ip, pwd, pwd, 'mysql');
				print (u'{}[+] {}:3306  Mysql weak password: root  {}{}'.format(G, ip, pwd, W));
				conn.close();
				break;
			except Exception as e:
				print(e)
				pass;
def main():
	mysql("zdy.anasit.com");
	

if __name__ == '__main__':
	main()