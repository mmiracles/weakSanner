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


def ftpConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            ftpScanner = FTPScanner(host, port,debugLogLevel=debugLogLevel)
            ftpRes = ftpScanner.scanWeakPwsd(pwdLines)
            resultFile.write(ftpRes)
    except Exception as e:
        print('ftpConnectError:', e)


def telnetConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            telnetScanner = TelnetScanner(host, port,debugLogLevel=debugLogLevel)
            telnetRes = telnetScanner.scanWeakPwsd(pwdLines)
            resultFile.write(telnetRes)
    except Exception as e:
        print('telnetConnectError:', e)


def sshConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            sshScanner = SSHScanner(host,port,debugLogLevel=debugLogLevel)
            sshRes = sshScanner.scanWeakPwsd(pwdLines)
            resultFile.write(sshRes)
    except Exception as e:
        print('sshConnectError:', e) 


def mysqlConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            mysqlScanner = MysqlScanner(host,port,debugLogLevel=debugLogLevel)
            mysqlRes = mysqlScanner.scanWeakPwsd(pwdLines)
            resultFile.write(mysqlRes)
    except Exception as e:
        print('mysqlConnectError:', e)


def postgresConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            pgScanner = PostgresScanner(host,port,debugLogLevel=debugLogLevel)
            pgRes = pgScanner.scanWeakPwsd(pwdLines)
            resultFile.write(pgRes)
    except Exception as e:
        print('pgsqlConnectError:', e)


def mongoConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            mongoScanner = MongoScanner(host,port,debugLogLevel=debugLogLevel)
            mongoRes = mongoScanner.scanWeakPwsd(pwdLines)
            resultFile.write(mongoRes)
    except Exception as e:
        print('mongoConnectError:', e)


def redisConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            redisScanner = RedisScanner(host,port,debugLogLevel=debugLogLevel)
            redisRes = redisScanner.scanWeakPwsd(pwdLines)
            resultFile.write(redisRes)
    except Exception as e:
        print('redisConnectError:', e)


def sqlServerConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            sqlScanner = SqlServerScanner(host,port,debugLogLevel=debugLogLevel)
            sqlRes = sqlScanner.scanWeakPwsd(pwdLines)
            resultFile.write(sqlRes)
    except Exception as e:
        print('sqlServerConnectError:', e)


def tomcatConnect(host, pwdLines,debugLogLevel,port):
    try:
        with open(resultFileDictionary, 'a') as resultFile:
            tomcatScanner = TomcatScanner(host,port,debugLogLevel=debugLogLevel)
            tomcatRes = tomcatScanner.scanWeakPwsd(pwdLines)
            resultFile.write(tomcatRes)
    except Exception as e:
        print('tomcatConnectError:', e)

def scanServices(services,host, pwdLines,debugLogLevel,port):
    if 'mysql' in services:
        threading.Thread(target=mysqlConnect, args=(host, pwdLines,debugLogLevel,port)).start()
    if 'ftp' in services:
        threading.Thread(target=ftpConnect, args=(host, pwdLines,debugLogLevel,port)).start()
    if 'telnet' in services:
        threading.Thread(target=telnetConnect, args=(host, pwdLines,debugLogLevel,port)).start()
    if 'ssh' in services:
        threading.Thread(target=sshConnect, args=(host, pwdLines,debugLogLevel,port)).start()
    if 'postgres' in services:
        threading.Thread(target=postgresConnect, args=(host, pwdLines,debugLogLevel,port)).start()
    if 'mongo' in services:
        threading.Thread(target=mongoConnect, args=(host, pwdLines,debugLogLevel,port)).start()
    if 'redis' in services:
        threading.Thread(target=redisConnect,args=(host, pwdLines,debugLogLevel,port)).start()
    if 'tomcat' in services:
        threading.Thread(target=tomcatConnect, args=(host, pwdLines,debugLogLevel,port)).start()
    if 'sqlServer' in services or 'sqlserver' in services:
        threading.Thread(target=sqlServerConnect, args=(host, pwdLines,debugLogLevel,port)).start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LXM Scanner')
    parser.add_argument('-H', dest='hostname', help='The host name')
    parser.add_argument('-p', dest='pwdFile', help='Password dictionary file')
    parser.add_argument('-r', dest='resultFile', help='Result dictionary file')
    parser.add_argument('-port', dest='port', help='The port or ports with "/" space for one service,example 1/80(only used in one service)')
    parser.add_argument('-s', dest='services', help='Services list with "," space,default all')
    parser.add_argument('-d', dest='debugLogLevel', help='debug log level: 1->simple  2->detail')
    params = parser.parse_args()

    host = params.hostname or HOST
    pwdFileDictionary = params.pwdFile or PWD_FILE
    resultFileDictionary = params.resultFile or RESULT_FILE
    debugLogLevel = int(params.debugLogLevel or DEBUG_LOG_LEVEL)
    services = []
    ports = [] # The range of ports like [1,80]
    if params.services:
        services = str(params.services).split(',')
    if services.__len__()==0:
        services = ALL_SERVICES
    if params.port:
        # If the port(s) is set but the number of services is more than 1,print tip and exit
        if services.__len__()>1:
            print('ERROR: If the port(s) is set,you must use -s to set only one service')
            exit(0)
        ports = list(map(int,params.port.split('/')))
        if ports.__len__()>2:
            print('the number of port(s) must be one or two')
            exit(0)
        if ports.__len__()==1:
            ports.append(ports[0])
        if ports[1]<ports[0]:
            print('invalid ports')
            exit(0)
    result = [] # weak password result list
    try:
        with open(pwdFileDictionary) as pwdFile, open(resultFileDictionary, 'a') as resultFile:
            # write localtime in result file
            resultFile.write('--------- LXM Scan Result At '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+' ---------\n')
            pwdLines = pwdFile.readlines()
            if(ports.__len__()==0):
                scanServices(services,host, pwdLines,debugLogLevel,None)
            else:
                for port in range(ports[0],ports[1]+1):
                    scanServices(services,host, pwdLines,debugLogLevel,port)
                    
    except Exception as e:
        print(e)
