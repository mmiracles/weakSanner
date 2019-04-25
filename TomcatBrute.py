#!/usr/bin/env python
# coding=utf-8

import logging
import urllib.request
import base64
# from xutils import encode_utf8

LOGIN_TIMEOUT = 12

class TomcatAuth:
    def __init__(self, host, port):
        self.addr = (host, port)
        self.url = "http://{}:{}".format(host, port)

    def login(self, username, password, timeout=LOGIN_TIMEOUT):
        conn_ok, auth_ok, banner = True, False, ''
        error_i = 0
        connection = None
        url = self.url
        flag_list = ['Application Manager', 'Welcome']

        try:
            login_url = url+'/manager/html'
            request = urllib.request.Request(login_url)
            auth_str_temp = username+b':'+password
            auth_str = base64.b64encode(auth_str_temp)
            request.add_header(b'Authorization', b'Basic '+auth_str)
            res = urllib.request.urlopen(request, timeout=LOGIN_TIMEOUT)
            res_code = res.code
            res_html = res.read()
        except urllib.request.HTTPError as e:
            res_code = e.code
            res_html = e.read()
        except urllib.request.URLError as e:
            error_i += 1
            if error_i >= 3:
                conn_ok = False
        print(username,password,res_code)
        if int(res_code) == 404:
            conn_ok = False
        elif int(res_code) == 401 or int(res_code) == 403:
            auth_ok = False
            conn_ok = True
        else:
            for flag in flag_list:
                if flag.encode() in res_html:
                    conn_ok = True
                    auth_ok = True
                    break
        return conn_ok, auth_ok, None


class TomcatBruteTester:
    def __init__(self, pwds, passwords=None):
        self.pwds = pwds
        pass

    def test(self, task):
        # pass
        (host, port) = (task[0], task[1])
        rs = []
        auth = TomcatAuth(host, port)
        for username in self.pwds:
            for password in self.pwds:
                pass
                conn_ok, auth_ok, other = auth.login(
                    username.strip('\n').strip('\n').encode(), password.strip('\n').strip('\n').encode())
                if not conn_ok:
                    return rs
                if not auth_ok:
                    continue
                rs.append([host, port, 'TomcatManager', username])
                print(rs)
                break
        if not rs:
            pass
            # logging.getLogger().info('SAFE %s:%d' % (host, port))
        return rs


if __name__ == '__main__':
    import sys
    # import xutils
    host, port = sys.argv[1], int(sys.argv[2])
    tester = TomcatBruteTester(open('pwd.txt').readlines())
    rs = tester.test((host,port))
    print(rs)
