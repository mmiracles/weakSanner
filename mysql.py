import pymysql
import threading


class MysqlScanner:
    def __init__(self, ip, port=3306):
        self.ip = ip
        self.port = port

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
                    info = 'mysql weak password: ip:{}:{},username:{},password:{}\n'.format(self.ip,self.port,username,password)
                    result += info
                    print(info)
        return result

if __name__ == '__main__':
    pass
