#!-----encoding:utf-8-------#


import socket
import time
import datetime
import binascii

#d=open('note3.txt','r')
#strlen=len(d.read())
#print(len(d.read()))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',23333))
s.listen(5)
print('start listening...')
while True:
    try:
        c,c_addr=s.accept()
        print('connected to：',c_addr)
        print('start receiving Time：')
        dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(dt)
        while True:
            data=c.recv(1024).decode('utf-8')
            #print(data)
            if not data:
                print('Finsh receiving Time：')
                dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                print(dt)
                break
        c.close()
    except KeyboardInterrupt:
        s.close()
        print('quit')
        break
s.close()
        

