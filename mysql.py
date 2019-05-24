import pymysql
import threading
import sys


class MysqlScanner:
    def __init__(self, ip, port,debugLogLevel=1):
        self.ip = ip
        self.port = port or 3306
        self.debugLogLevel = debugLogLevel

    def connect(self, username, password):
        try:
            conn = pymysql.connect(
                self.ip, username, password, port=self.port)
            conn.close()
            return 'success'
        except Exception as e:
            if(str(e).find('1045') == -1):
                # print(e)
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
                    info = 'mysql weak password for ip:{}:{},username:{},password:{}'.format(self.ip,self.port,username,password)
                    result += info + '\n'
                    print(info)
                elif self.debugLogLevel >= 2:
                    print('mysql connect {} for ip:{}:{},username:{},password:{}'.format(res,self.ip,self.port,username,password))
        return result

if __name__ == '__main__':
    pass
