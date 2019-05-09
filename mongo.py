import pymongo
import threading

class MongoScanner:
    def __init__(self,ip,port,debugLogLevel=1):
        self.ip = ip
        self.port = port or 27017
        self.debugLogLevel = debugLogLevel

    def connect(self,username,password):
        try:
            mongo = pymongo.MongoClient(
                'mongodb://{}:{}@{}:{}/'.format(username, password, self.ip,self.port))
            dblist = mongo.list_database_names()
            return 'success'
        except Exception as e:
            if('10061' in str(e) or 'out' in str(e)):
                return 'timeout'
            else:
                return 'fail'

    def scanWeakPwsd(self, pwdLines):
        result = ''
        for username in pwdLines:
            for password in pwdLines:
                username = username.strip('\r').strip('\n')
                password = password.strip('\r').strip('\n')
                res = self.connect(username, password)
                if res == 'success':
                    info = 'mongo weak password for ip:{}:{},username:{},password:{}'.format(self.ip,self.port,username,password)
                    result += info + '\n'
                    print(info)
                elif self.debugLogLevel >= 2:
                    print('mongo connect {} for ip:{}:{},username:{},password:{}'.format(res,self.ip,self.port,username,password))
        return result

if __name__ == '__main__':
    pass
