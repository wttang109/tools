# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:06:22 2019

@author: Sunny
"""

import socket
import time

rpm_input=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('******', 1234))
    
    while True:
        
        
        try:
            
            
            response = s.recv(1024)
            print('102 response: ', str(response))
            if 'xa2' in str(response)[:5]:

                s.recv(1024)
                s.sendall(rpm_input)
                print('102 send 0rpm ###############################')
                time.sleep(1)
                continue
            
        except socket.error:
            print ("get connect error as")
            continue
#        except KeyboardInterrupt:
#            pass
#        s.close()

if __name__ == '__main__':
    main()








'''
try:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('******', 1234))
        response = s.recv(1024)
        print('102 response: ', str(response))
        if str(response) != "b'R'":
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('******', 1234))
            s.recv(1024)
            s.sendall(rpm_input)
            s.close()
            print('102 send 0rpm')
            continue
except KeyboardInterrupt:
    pass
s.close()
'''