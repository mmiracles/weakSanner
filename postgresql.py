import psycopg2
import threading

class PostgresScanner:
    def __init__(self, ip, port=5432,debugLogLevel=1):
        self.ip = ip
        self.port = port
        self.debugLogLevel = debugLogLevel

    def connect(self, username,password):
        try:
            conn = psycopg2.connect(
                user=username, password=password, host=self.ip,port=self.port)
            cur = conn.cursor()
            conn.close()
            return 'success'
        except Exception as e:
            if(str(e).find('authentication')==-1):
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
                    info = 'pgsql weak password for ip:{}:{},username:{},password:{}'.format(self.ip,self.port,username,password)
                    result += info + '\n'
                    print(info)
                elif self.debugLogLevel >= 2:
                    print('pgsql connect {} for ip:{}:{},username:{},password:{}'.format(res,self.ip,self.port,username,password))
        return result
if __name__ == '__main__':
    pass
    # for ip3 in range(234, 235):
    #     for ip4 in range(254, 255):
    #         threading.Thread(target=postgresql, args=(
    #             '129.204.'+str(ip3)+'.' + str(ip4),)).start()
