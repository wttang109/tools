# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:42:53 2019

@author: Sunny
"""

#import socket
#hostname = '' #設定主機名 10.0.0.101
#port = 5566  #設定埠號 要確保這個埠號沒有被使用，可以在cmd裡面檢視
#addr = (hostname,port)
#srv = socket.socket() #建立一個socket
##srv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#srv.bind(addr)
#srv.bind((socket.gethostname(),5566))

'''
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.connect(('10.0.0.101', 5566))
connect_socket,client_addr = srv.accept()
recevent = connect_socket.recv(1024)
print(str(recevent,encoding='gbk'))

srv.listen(2)
print("waitting connect")
while True:
    connect_socket,client_addr = srv.accept()
    print(client_addr, 'is connecting')
    recevent = connect_socket.recv(1024)
    print(str(recevent,encoding='gbk'))
    connect_socket.send(bytes("transmission done",encoding='gbk'))
    if str(recevent,encoding='gbk')=='exit':
        break
connect_socket.close()
'''

rpm400 =  bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x90\x01\x99\x00')
rpm200 =  bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\xc8\x00\xd0\x00')
rpm100 =  bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x64\x00\x6c\x00')
rpm0   =  bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')

# Echo client program

import socket

def main(HOST,PORT,rpm):
    
    if rpm == rpm400:
        name='rpm400'
    elif rpm == rpm200:
        name='rpm200'
    elif rpm == rpm100:
        name='rpm100'
    elif rpm == rpm0:
        name='rpm0'
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
#    s.connect(('10.0.0.101', PORT))
    #    msg = rpm
    while True:
        sss1=s.recv(1024)
        print('sss1',repr(sss1))
    
    
    sss2=s.recv(1024)
    print('sss2',repr(sss2))
    sss3=s.recv(1024)
    print('sss3',repr(sss3))
    sss4=s.recv(1024)
    print('sss4',repr(sss4))
    sss5=s.recv(1024)
    print('sss5',repr(sss5))
    sss6=s.recv(1024)
    print('sss6',repr(sss6))
    sss7=s.recv(1024)
    print('sss7',repr(sss7))
    sss8=s.recv(1024)
    print('sss8',repr(sss8))
    sss9=s.recv(1024)
    print('sss9',repr(sss9))
    sss10=s.recv(1024)
    print('sss10',repr(sss10))
    sss11=s.recv(1024)
    print('sss11',repr(sss11))
    s.sendall(rpm)
    print ('Send', HOST, name)
    data = s.recv(1024)
    s.close()
#    print(repr(data))
    if repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08\\x90\\x01\\x99\\x00'":
        print (HOST, 'Received', '400rpm')
    elif repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08\\xc8\\x00\\xd0\\x00'":
        print (HOST, 'Received', '200rpm')
    elif repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08d\\x00l\\x00'":
        print (HOST, 'Received', '100rpm')
    elif repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08\\x00\\x00\\x08\\x00'":
        print (HOST,'Received', '0rpm')


'''
#### Austin ###################################################
HOST1 = '10.0.0.101'    # The remote host
PORT1 = 5566              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
s.connect((HOST1, PORT1))
#s.connect((HOST2, PORT2))

sss=s.recv(1024)
print(str(sss))
#print(type(sss))
msg = bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')

s.sendall(msg)
print ('send ', repr(msg))
data = s.recv(1024)

#while True:
#    data = s.recv(1024)
#    print ('Received', repr(data))
s.close()
if repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08\\x00\\x00\\x08\\x00'":
    print ('Received', '0rpm')
#print ('Received', repr(data))

####################################################################

HOST2 = '10.0.0.102'    # The remote host
PORT2 = 5566              # The same port as used by the server
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((HOST2, PORT2))
ddd=s1.recv(1024)
print(str(ddd))
print(type(ddd))
msg1 = bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x90\x01\x99\x00')
s1.sendall(msg1)
print ('send1 ', repr(msg1))
data1 = s1.recv(1024)
s1.close()
print ('Received1', repr(data1))


'''
'''
import socket, select
socks = {}
# Connect to different servers here #
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socks[sock1.fileno()] = sock1
poll = select.poll()
for sock in socks:
    poll.register(sock)
while 1:
    fd, event = poll.poll() # Optional timeout parameter in seconds
    sock = socks[fd]
    sock.recv(1024) # Do stuff
'''
'''
#### Austin ##################################################
'''

#import socket
#import threading
#import time

'''
def handle(conn_addr):
    print("Someone Connected")
    time.sleep(4)
    print("And now I die")


host = socket.gethostname()
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((host,port))
    print('bind is done')
except socket.error as e:
    print(str(e))

s.listen(2)
print('listen is done')
while True:
#    threading.Thread(handle(s.accept())).start()
    print('start accept')
    threading.Thread(target=handle, args=(s.accept(),)).start()
    print('accept is done')

print("Should never be reached")

def serverwaiter():
    host = socket.gethostname()
    port = 6027
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((host,port))
    s.listen(10)
    while True:
        cobj,addr = s.accept()
        mythread = threading.Thread(target=client,name='TCP client {}'.format(threading.active_count()-1),args=(cobj,addr))
        mythread.daemon = True # So client threads die on main thread exit.
        mythread.start()

def client(cobj,addr):
    print('Connected to',addr)
    while True:
        data = cobj.recv(1024)
        if not data: break
        print('Host {} sent data = {}'.format(addr,data.decode()))
    cobj.close()

serverwaiter()
'''

if __name__=='__main__':
    main('10.0.0.101',5566,rpm0)
#    main('10.0.0.102',5566,rpm0)




