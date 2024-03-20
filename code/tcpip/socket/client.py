#!-----encoding:utf-8-------#
import socket
import time
import datetime
import binascii
msg=open('note.txt','r')
#buf='qwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuioqwertyuio'
buf=msg.read()
strlen=len(buf)
print(strlen)
#print(msg.read())
msg.close()
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',23333))
print('connected to server...')
dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print('start send:',dt)
client.send(buf.encode('utf-8'))
dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print('stop send:',dt)
client.close()

        

