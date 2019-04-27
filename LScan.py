from ftp import FTPScanner
from telnet import TelnetScanner
from ssh import SSHScanner
from mysql import MysqlScanner
from postgresql import PostgresScanner
from mongo import MongoScanner
import threading

ip = '129.204.234.135'
username = 'admin'
password = 'admin'


def ftpConnect(ip, username, password):
    ftpSanner = FTPScanner(ip, 22)
    ftpRes = ftpSanner.login(username, password)
    print('ftp:', ftpRes)


def telnetConnect(ip, username, password):
    telnetScanner = TelnetScanner(ip, 23)
    telnetRes = telnetScanner.connectTelnet(username, password)
    print('telnet:', telnetRes)


def sshConnect(ip, username, password):
    sshScanner = SSHScanner(ip)
    sshRes = sshScanner.connectSSH(username, password)
    print('ssh:', sshRes)


def mysqlConnect(ip, username, password):
    mysqlScanner = MysqlScanner(ip)
    mysqlRes = mysqlScanner.connect(username, password)
    print('mysql:', mysqlRes)


def postgresConnect(ip, username, password):
    pgScanner = PostgresScanner(ip)
    pgRes = pgScanner.connect(username, password)
    print('pgsql:', pgRes)

def mongoConnect(ip, username, password):
    mongoScanner = MongoScanner(ip)
    mongoRes = mongoScanner.connect(username, password)
    print('mongo:', mongoRes)

threading.Thread(target=ftpConnect, args=(ip, username, password,)).start()
threading.Thread(target=telnetConnect, args=(ip, username, password,)).start()
threading.Thread(target=sshConnect, args=(ip, username, password,)).start()
threading.Thread(target=mysqlConnect, args=(ip, username, password,)).start()
threading.Thread(target=postgresConnect, args=(ip, username, password,)).start()
threading.Thread(target=mongoConnect, args=(ip, username, password,)).start()
