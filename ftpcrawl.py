#!/usr/bin/env python3
from ftplib import FTP
import argparse
parser = argparse.ArgumentParser(prog='Simple FTP crawler POC')
parser.add_argument('-H','--host',help='The FTP site to be crawled',required=True)
parser.add_argument('-u','--user',help='Username to be used',default='anonymous')
parser.add_argument('-p','--password',help='The password to be used',default='anonymous')
args = parser.parse_args()
host = args.host
user = args.user
password = args.password
ftp = FTP(host)
ftp.login()
files = []
fm = ftp.retrlines('LIST',files.append)
try:
    for fd in files:
        kd=str(fd).split(' ')
        if kd[0].startswith('d'):
            print(kd[-1])
            ftp.dir(kd[-1])
except Exception as e:
    print(str(e))
