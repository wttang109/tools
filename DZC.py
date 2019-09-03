# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 08:58:13 2019

@author: Sunny
"""

# =============================================================================
# rpm400 =  bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x90\x01\x99\x00')
# rpm200 =  bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\xc8\x00\xd0\x00')
# rpm100 =  bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x64\x00\x6c\x00')
# rpm0   =  bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')
# 
# =============================================================================
import socket
#import select

#timeout = 300 * 1

def main(HOST,rpm):
    
    if rpm == 'r400':
        rpm_input=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x90\x01\x99\x00')
    elif rpm == 'r200':
        rpm_input=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\xc8\x00\xd0\x00')
    elif rpm == 'r100':
        rpm_input=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x64\x00\x6c\x00')
    elif rpm == 'r0':
        rpm_input=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')
    elif rpm == 'exit':
        rpm_input=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')

#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    s.connect((HOST, PORT))
    s.recv(1024)
#    msg = rpm
    s.sendall(rpm_input)
#    s.setblocking(0),,
    print ('Send', HOST, rpm)
#    r, _, _ = select.select([s], [], [])
    if r:
        data = s.recv(1024)#.strip('\x00')
    else:
        print('recv error')
    

#    data = s.recv(1024)

    print ('data',repr(data))
#    print(repr(data))
    if repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08\\x90\\x01\\x99\\x00'":
        print (HOST, 'Received', '400rpm')
    elif repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08\\xc8\\x00\\xd0\\x00'":
        print (HOST, 'Received', '200rpm')
    elif repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08d\\x00l\\x00'":
        print (HOST, 'Received', '100rpm')
    elif repr(data)=="b'\\xa1\\x00\\x00\\x00U\\x03\\x08\\x00\\x00\\x08\\x00'":
        print (HOST,'Received', '0rpm')
    
    
if __name__=='__main__':
    
    while True:
        r = input('r: ')
        h = input('h: ')
        HOST='*****.{}'.format(h)
        PORT=1234
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        
        main(HOST,r)
        print('-----------------------')
#        main('*****',1234,rpm0)
        if r =='exit':
            s.close()
            break
    
    
    
    
    
    
    