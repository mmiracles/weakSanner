import redis


class RedisScanner:
    def __init__(self, ip, port=6379,debugLogLevel=1):
        self.ip = ip
        self.port = port
        self.debugLogLevel = debugLogLevel

    def connect(self,  password):
        try:
            r = redis.Redis(host=self.ip,port=self.port,password=password)
            r.get('test')
            return 'success'
        except Exception as e:
            if 'invalid' in str(e) or 'NOAUTH' in str(e):
                return 'fail'
            else:
                return 'timeout'

    def scanWeakPwsd(self, pwdLines):
        result = ''
        for password in pwdLines:
            password = password.strip('\r').strip('\n')
            res = self.connect(password)
            print(password,res)
            if res == 'success':
                info = 'redis weak password for ip:{}:{},password:{}'.format(self.ip,self.port,password)
                result += info + '\n'
                print(info)
            elif self.debugLogLevel >= 2:
                    print('redis connect {} for ip:{}:{},password:{}'.format(res,self.ip,self.port,password))
        return result

if __name__ == '__main__':
    pass