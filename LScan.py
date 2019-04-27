from ftp import FTPScanner
from telnet import TelnetScanner
from ssh import SSHScanner
from mysql import MysqlScanner
from postgresql import PostgresScanner
from mongo import MongoScanner
from pyredis import RedisScanner
from sqlserver import SqlServerScanner
from tomcat import TomcatScanner
import argparse
import threading

RESULT_FILE = './result.txt'
PWD_FILE = './pwdTest.txt'


def ftpConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            ftpSanner = FTPScanner(host, 22)
            ftpRes = ftpSanner.scanWeakPwsd(pwdLines)
            resultFile.write(ftpRes)
    except Exception as e:
        print('ftpConnectError:', e)


def telnetConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            telnetScanner = TelnetScanner(host, 23)
            telnetRes = telnetScanner.scanWeakPwsd(pwdLines)
            resultFile.write(telnetRes)
    except Exception as e:
        print('telnetConnectError:', e)


def sshConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            sshScanner = SSHScanner(host)
            sshRes = sshScanner.scanWeakPwsd(pwdLines)
            resultFile.write(sshRes)
    except Exception as e:
        print('sshConnectError:', e)


def mysqlConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            mysqlScanner = MysqlScanner(host)
            mysqlRes = mysqlScanner.scanWeakPwsd(pwdLines)
            resultFile.write(mysqlRes)
    except Exception as e:
        print('mysqlConnectError:', e)


def postgresConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            pgScanner = PostgresScanner(host)
            pgRes = pgScanner.scanWeakPwsd(pwdLines)
            resultFile.write(pgRes)
    except Exception as e:
        print('pgsqlConnectError:', e)


def mongoConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            mongoScanner = MongoScanner(host)
            mongoRes = mongoScanner.scanWeakPwsd(pwdLines)
            resultFile.write(mongoRes)
    except Exception as e:
        print('mongoConnectError:', e)


def redisConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            redisScanner = RedisScanner(host)
            redisRes = redisScanner.scanWeakPwsd(pwdLines)
            resultFile.write(redisRes)
    except Exception as e:
        print('redisConnectError:', e)


def sqlServerConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            sqlScanner = SqlServerScanner(host)
            sqlRes = sqlScanner.scanWeakPwsd(pwdLines)
            resultFile.write(sqlRes)
    except Exception as e:
        print('sqlServerConnectError:', e)


def tomcatConnect(host, pwdLines):
    try:
        with open(RESULT_FILE, 'a') as resultFile:
            tomcatScanner = TomcatScanner(host)
            tomcatRes = tomcatScanner.scanWeakPwsd(pwdLines)
            resultFile.write(tomcatRes)
    except Exception as e:
        print('tomcatConnectError:', e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LXM Scanner')
    parser.add_argument('-H', dest='hostname', help='The host name')
    parser.add_argument('-f', dest='pwdFile', help='Password dictionary file')
    parser.add_argument('-r', dest='resultFile', help='Result dictionary file')
    params = None
    try:
        params = parser.parse_args()
    except:
        print(parser.parse_args(['-h']))
        exit(0)

    host = str(params.hostname)
    if params.pwdFile:
        pwdFile = params.pwdFile
    if host == 'None':
        print(parser.parse_args(['-h']))
        exit(0)

    result = []
    try:
        with open(PWD_FILE) as pwdFile:
            pwdLines = pwdFile.readlines()
            # threading.Thread(target=ftpConnect, args=(host, pwdLines)).start()
            # threading.Thread(target=telnetConnect, args=(host, pwdLines)).start()
            # threading.Thread(target=sshConnect, args=(host, pwdLines)).start()
            threading.Thread(target=mysqlConnect, args=(host, pwdLines)).start()
            # threading.Thread(target=postgresConnect, args=(host, pwdLines)).start()
            # threading.Thread(target=mongoConnect, args=(host, pwdLines)).start()
            threading.Thread(target=redisConnect,
                             args=(host, pwdLines)).start()
            # threading.Thread(target=tomcatConnect, args=(host, pwdLines)).start()
            # threading.Thread(target=sqlServerConnect, args=(host, pwdLines)).start()
    except Exception as e:
        print(e)
