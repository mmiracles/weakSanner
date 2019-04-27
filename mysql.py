import pymysql
import threading
import sys


class MysqlScanner:
    def __init__(self, ip, port=3306,debugLogLevel=1):
        self.ip = ip
        self.port = port
        self.debugLogLevel = debugLogLevel

    def connect(self, username, password):
        try:
            conn = pymysql.connect(
                self.ip, username, password, 'mysql', self.port)
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
                    print('\033[1;32;40m')
                    info = 'mysql weak password for ip:{}:{},username:{},password:{}'.format(self.ip,self.port,username,password)
                    result += info + '\n'
                    print(info)
                    print('\033[0m')
                elif self.debugLogLevel >= 2:
                    print('mysql connect {} for ip:{}:{},username:{},password:{}'.format(res,self.ip,self.port,username,password))
        return result

if __name__ == '__main__':
    pass
