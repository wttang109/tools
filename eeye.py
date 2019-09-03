# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:31:38 2019

@author: Sunny
"""

import socket
import time
import threading
import c101
rpm_input=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('******', 1234))
s.recv(1024)
s.sendall(bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x90\x01\x99\x00'))
s.close()
'''

'''
def main():
    def c101(host='101'):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('***.{}'.format(host), 1234))
        while True:
            try:
                response = s.recv(1024)
                print('{} response: '.format(host), str(response))
                if 'xa2' in str(response)[:5]:
                    s.recv(1024)
                    s.sendall(rpm_input)
                    print('{} send 0rpm ###############################'.format(host))
                    time.sleep(1)
                    continue
            except socket.error:
                print ("get connect error as")
                continue
    def c102(host='102'):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('***{}'.format(host), 456))
        while True:
            try:
                response = s.recv(1024)
                print('{} response: '.format(host), str(response))
                if 'xa2' in str(response)[:5]:
                    s.recv(1024)
                    s.sendall(rpm_input)
                    print('{} send 0rpm ###############################'.format(host))
                    time.sleep(1)
                    continue
            except socket.error:
                print ("get connect error as")
                continue
    threading.Thread(target=c101()).start()
    threading.Thread(target=c102()).start()
'''

def main():
    
    while True:
        a=c101.main()
        print(a)
        if a==38:
            print('get xa2 and stop')
            
    




if __name__ == '__main__':
    main()


