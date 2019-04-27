import socket
import binascii
import threading
import pymssql

import redis


class SqlServerScanner:
    def __init__(self, ip, port=6379):
        self.ip = ip
        self.port = port

    def connect(self, username, password):
        try:
            conn = pymssql.connect(server=self.ip, port=self.port,user=username, password=password,login_timeout=10)
            cursor = conn.cursor()
            if not cursor:
                return 'fail'
            else:
                return 'success'
        except Exception as e:
            if('18456' in str(e)):
                return 'fail'
            else:
                return 'timeout'

    def scanWeakPwsd(self, pwdLines):
        result = ''
        for username in pwdLines:
            for password in pwdLines:
                username = username.strip('\r').strip('\n')
                password = password.strip('\r').strip('\n')
                res = self.connect(username, password)
                print(res)
                if res == 'success':
                    info = 'sqlServer weak password: ip:{}:{},username:{},password:{}\n'.format(self.ip,self.port,username,password)
                    result += info
                    print(info)
        return result

if __name__ == '__main__':
    pass