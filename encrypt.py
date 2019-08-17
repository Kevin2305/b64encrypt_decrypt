#!/usr/bin/env python
# coding: utf-8
import base64
import getpass
import time
import logging
dfmt="%Y-%m-%d %H:%M:%S"
fmt="%(asctime)s %(levelname)s : %(message)s"
level=logging.INFO
logging.basicConfig(filename="log.log",level=level,format=fmt,datefmt=dfmt)
'''
pwd=getpass.getpass('Type the password to convert: ')
pwd=base64.b64encode(pwd.encode('utf-8'))
with open('pwd.txt','wb') as f:
    f.write(pwd)
print("Password Stored!")
#time.sleep(5)
'''
while True:
    a=input("input jiami or jiemi or quit:")
    if a =='jiami':
        aw=input("shu ru ming wen: ")
        try:
            s=base64.b64encode(aw.encode('utf-8')).decode('utf-8')
        except Exception:
            logging.warning("ming wen cuo le!")
        print(s)
        logging.info(s)
    if a =='jiemi':
        bw=input("shu ru mi wen: ")
        try:
            s=base64.b64decode(bw).decode('utf-8')
        except Exception:
            logging.warning("mi wen cuo le!")
        print(s)
        logging.info(s)
    if a =='quit':
        break
    