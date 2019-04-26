from ftp import FTPScanner
from telnet import TelnetScanner
from ssh import SSHScanner
from mysql import MysqlScanner
from postgresql import PostgresScanner
from mongo import MongoScanner
from pyredis import RedisScanner
from sqlserver import SqlServerScanner
from tomcat import TomcatScanner

import threading

ip = '129.204.234.135'
username = 'admin'
password = 'admin'


def ftpConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            ftpSanner = FTPScanner(ip, 22)
            ftpRes = ftpSanner.scanWeakPwsd(pwdLines)
            resultFile.write(ftpRes)
            print(ftpRes)
    except Exception as e:
        print('ftpConnectError:', e)


def telnetConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            telnetScanner = TelnetScanner(ip, 23)
            telnetRes = telnetScanner.scanWeakPwsd(pwdLines)
            resultFile.write(telnetRes)
    except Exception as e:
        print('telnetConnectError:', e)


def sshConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            sshScanner = SSHScanner(ip)
            sshRes = sshScanner.scanWeakPwsd(pwdLines)
            resultFile.write(sshRes)
    except Exception as e:
        print('sshConnectError:', e)


def mysqlConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            mysqlScanner = MysqlScanner(ip)
            mysqlRes = mysqlScanner.scanWeakPwsd(pwdLines)
            resultFile.write(mysqlRes)
    except Exception as e:
        print('mysqlConnectError:', e)


def postgresConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            pgScanner = PostgresScanner(ip)
            pgRes = pgScanner.scanWeakPwsd(pwdLines)
            resultFile.write(pgRes)
    except Exception as e:
        print('pgsqlConnectError:', e)


def mongoConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            mongoScanner = MongoScanner(ip)
            mongoRes = mongoScanner.scanWeakPwsd(pwdLines)
            resultFile.write(mongoRes)
    except Exception as e:
        print('mongoConnectError:', e)

def redisConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            redisScanner = RedisScanner(ip)
            redisRes = redisScanner.scanWeakPwsd(pwdLines)
            resultFile.write(redisRes)
    except Exception as e:
        print('redisConnectError:', e)

def sqlServerConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            sqlScanner = SqlServerScanner(ip)
            sqlRes = sqlScanner.scanWeakPwsd(pwdLines)
            resultFile.write(sqlRes)
    except Exception as e:
        print('sqlServerConnectError:', e)
    
def tomcatConnect(ip, pwdLines):
    try:
        with open('./result.txt', 'a') as resultFile:
            tomcatScanner = TomcatScanner(ip)
            tomcatRes = tomcatScanner.scanWeakPwsd(pwdLines)
            resultFile.write(tomcatRes)
    except Exception as e:
        print('tomcatConnectError:', e)

result = []
try:
    with open('./pwdTest.txt') as pwdFile:
        pwdLines = pwdFile.readlines()
        # threading.Thread(target=ftpConnect, args=(ip, pwdLines)).start()
        # threading.Thread(target=telnetConnect, args=(ip, pwdLines)).start()
        # threading.Thread(target=sshConnect, args=(ip, pwdLines)).start()
        # threading.Thread(target=mysqlConnect, args=(ip, pwdLines)).start()
        # threading.Thread(target=postgresConnect, args=(ip, pwdLines)).start()
        # threading.Thread(target=mongoConnect, args=(ip, pwdLines)).start()
        threading.Thread(target=redisConnect, args=(ip, pwdLines)).start()
        threading.Thread(target=tomcatConnect, args=(ip, pwdLines)).start()
        # threading.Thread(target=sqlServerConnect, args=(ip, pwdLines)).start()
except Exception as e:
    print(e)
