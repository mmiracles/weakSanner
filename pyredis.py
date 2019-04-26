import redis


class RedisScanner:
    def __init__(self, ip, port=6379):
        self.ip = ip
        self.port = port

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
            if res == 'success':
                info = 'redis weak password: ip:{}:{},password:{}\n'.format(self.ip,self.port,password)
                result += info
                print(info)
        return result

if __name__ == '__main__':
    pass