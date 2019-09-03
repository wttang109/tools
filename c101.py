# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:01:47 2019

@author: Sunny
原文链接：https://blog.csdn.net/xiemanR/article/details/53192222
"""

import socket
import time

rpm_input=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('******', 123))
    
    while True:
#        try:
        response = s.recv(1024)
        print('101 response: ', str(response))
        
        if 'xa2' in str(response)[:6]:

#            s.recv(1024)
            s.sendall(rpm_input)
            print('101 send 0rpm ###############################')
            s.close()
            time.sleep(1)
            break
#        except socket.error:
#            print ("get connect error as")
#            continue
#        except KeyboardInterrupt:
#            pass
    
    return 38

if __name__ == '__main__':
    main()

    
    
'''
try:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('******', 1234))
        response = s.recv(1024)
        print('101 response: ', str(response))
        if str(response) != "b'R'":
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('******', 1234))
            s.recv(1024)
            s.sendall(rpm_input)
            s.close()
            print('101 send 0rpm')
            continue
except KeyboardInterrupt:
    pass
s.close()
'''