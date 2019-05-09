#!/usr/bin/env python
# coding=utf-8

import logging
import urllib.request
import base64
import time

# from xutils import encode_utf8

LOGIN_TIMEOUT = 12


class TomcatScanner:
    def __init__(self, ip, port,debugLogLevel=1):
        self.ip = ip
        self.port = port or 8080
        self.debugLogLevel = debugLogLevel
        self.url = "http://{}:{}".format(ip, port)

    def login(self, username, password, timeout=LOGIN_TIMEOUT):
        error_i = 0
        flag_list = ['Application Manager', 'Welcome']
        res_code = 0
        res_html = ''
        try:
            login_url = self.url+'/manager/html'
            request = urllib.request.Request(login_url)
            auth_str_temp = username.encode()+b':'+password.encode()
            auth_str = base64.b64encode(auth_str_temp)
            request.add_header(b'Authorization', b'Basic '+auth_str)
            res = urllib.request.urlopen(request, timeout=LOGIN_TIMEOUT)
            res_code = 200
            res_html = res.read()
        except urllib.request.HTTPError as e:
            res_code = e.code
            res_html = e.read()
        except urllib.request.URLError as e:
            error_i += 1
            if error_i >= 3:
                return 'timeout'
        if int(res_code) == 404:
            return 'timeout'
        elif int(res_code) == 401 or int(res_code) == 403:
            return 'fail'
        elif int(res_code) == 200:
            for flag in flag_list:
                if flag.encode() in res_html:
                    return 'success'
            return 'fail'

    def scanWeakPwsd(self, pwdLines):
        result = ''
        for username in pwdLines:
            for password in pwdLines:
                username = username.strip('\r').strip('\n')
                password = password.strip('\r').strip('\n')
                res = self.login(username, password)
                if res == 'success':
                    info = 'tomcat weak password for ip:{}:{},username:{},password:{}'.format(
                        self.ip, self.port, username, password)
                    result += info + '\n'
                    print(info)
                elif self.debugLogLevel >= 2:
                    print('tomcat connect {} for ip:{}:{},username:{},password:{}'.format(res,self.ip,self.port,username,password))
                time.sleep(0.5)
        return result


if __name__ == '__main__':
    import sys
    # import xutils
    # host, port = sys.argv[1], int(sys.argv[2])
    # tester = TomcatBruteTester(open('pwd.txt').readlines())
    # rs = tester.test((host,port))
    # print(rs)
