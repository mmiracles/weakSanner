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
import time
import threading

HOST = '127.0.0.1'
RESULT_FILE = './result.txt'
PWD_FILE = './pwdTest.txt'
ALL_SERVICES = ['ftp','telnet','ssh','mysql','redis','mongo','postgres','sqlserver','tomcat']
DEBUG_LOG_LEVEL = 1 # 1->simple  3->detail

def ftpConnect(host, pwdLines):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            ftpScanner = FTPScanner(host, port=22,debugLogLevel=debugLogLevel)
            ftpRes = ftpScanner.scanWeakPwsd(pwdLines)
            resultFile.write(ftpRes)
    except Exception as e:
        print('ftpConnectError:', e)


def telnetConnect(host, pwdLines):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            telnetScanner = TelnetScanner(host, 23,debugLogLevel=debugLogLevel)
            telnetRes = telnetScanner.scanWeakPwsd(pwdLines)
            resultFile.write(telnetRes)
    except Exception as e:
        print('telnetConnectError:', e)


def sshConnect(host, pwdLines):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            sshScanner = SSHScanner(host,debugLogLevel=debugLogLevel)
            sshRes = sshScanner.scanWeakPwsd(pwdLines)
            resultFile.write(sshRes)
    except Exception as e:
        print('sshConnectError:', e) 


def mysqlConnect(host, pwdLines,debugLogLevel):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            mysqlScanner = MysqlScanner(host,debugLogLevel=debugLogLevel)
            mysqlRes = mysqlScanner.scanWeakPwsd(pwdLines)
            resultFile.write(mysqlRes)
    except Exception as e:
        print('mysqlConnectError:', e)


def postgresConnect(host, pwdLines):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            pgScanner = PostgresScanner(host,debugLogLevel=debugLogLevel)
            pgRes = pgScanner.scanWeakPwsd(pwdLines)
            resultFile.write(pgRes)
    except Exception as e:
        print('pgsqlConnectError:', e)


def mongoConnect(host, pwdLines):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            mongoScanner = MongoScanner(host,debugLogLevel=debugLogLevel)
            mongoRes = mongoScanner.scanWeakPwsd(pwdLines)
            resultFile.write(mongoRes)
    except Exception as e:
        print('mongoConnectError:', e)


def redisConnect(host, pwdLines):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            print(debugLogLevel)
            redisScanner = RedisScanner(host,debugLogLevel=debugLogLevel)
            redisRes = redisScanner.scanWeakPwsd(pwdLines)
            resultFile.write(redisRes)
    except Exception as e:
        print('redisConnectError:', e)


def sqlServerConnect(host, pwdLines):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            sqlScanner = SqlServerScanner(host,debugLogLevel=debugLogLevel)
            sqlRes = sqlScanner.scanWeakPwsd(pwdLines)
            resultFile.write(sqlRes)
    except Exception as e:
        print('sqlServerConnectError:', e)


def tomcatConnect(host, pwdLines):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            tomcatScanner = TomcatScanner(host,debugLogLevel=debugLogLevel)
            tomcatRes = tomcatScanner.scanWeakPwsd(pwdLines)
            resultFile.write(tomcatRes)
    except Exception as e:
        print('tomcatConnectError:', e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LXM Scanner')
    parser.add_argument('-H', dest='hostname', help='The host name')
    parser.add_argument('-p', dest='pwdFile', help='Password dictionary file')
    parser.add_argument('-r', dest='resultFile', help='Result dictionary file')
    parser.add_argument('-s', dest='services', help='Services list with "," space,default all')
    parser.add_argument('-d', dest='debugLogLevel', help='debug log level: 1->simple  2->detail')
    params = None
    try:
        params = parser.parse_args()
    except:
        print(parser.parse_args(['-h']))
        exit(0)

    host = params.hostname or HOST
    pwdFileDictionary = params.pwdFile or PWD_FILE
    resultFileDictionary = params.resultFile or RESULT_FILE
    debugLogLevel = int(params.debugLogLevel or DEBUG_LOG_LEVEL)
    services = []
    if params.services:
        services = str(params.services).split(',')
    if services.__len__()==0:
        services = ALL_SERVICES

    result = [] # weak password result list
    try:
        with open(pwdFileDictionary) as pwdFile, open(resultFileDictionary, 'a') as resultFile:
            # write localtime in result file
            resultFile.write('--------- LXM Scan Result At '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+' ---------\n')
            pwdLines = pwdFile.readlines()
            if 'mysql' in services:
                threading.Thread(target=mysqlConnect, args=(host, pwdLines,debugLogLevel)).start()
            if 'ftp' in services:
                threading.Thread(target=ftpConnect, args=(host, pwdLines)).start()
            if 'telnet' in services:
                threading.Thread(target=telnetConnect, args=(host, pwdLines)).start()
            if 'ssh' in services:
                threading.Thread(target=sshConnect, args=(host, pwdLines)).start()
            if 'postgres' in services:
                threading.Thread(target=postgresConnect, args=(host, pwdLines)).start()
            if 'mongo' in services:
                threading.Thread(target=mongoConnect, args=(host, pwdLines)).start()
            if 'redis' in services:
                threading.Thread(target=redisConnect,args=(host, pwdLines)).start()
            if 'tomcat' in services:
                threading.Thread(target=tomcatConnect, args=(host, pwdLines)).start()
            if 'sqlServer' in services or 'sqlserver' in services:
                threading.Thread(target=sqlServerConnect, args=(host, pwdLines)).start()
    except Exception as e:
        print(e)
