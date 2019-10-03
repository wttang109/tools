# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:18:46 2019

@author: Sunny
"""
#import SmartConvey_mian_def
import multiprocessing
#from multiprocessing import *
#from multiprocessing import Queue
#from multiprocessing import Process
#import threading
import time
import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import modbus_tk.defines as cst

#Get Motor 0 Config Speed	0x55 0x03 0x08 0x01 0x00 0x09 0x00
#Get Motor 1 Config Speed	0x55 0x03 0x08 0x11 0x00 0x19 0x00
# =============================================================================
# s1.connect()
# s2.connect()
# r = s1.recv()
# s2.sendall(r)
# =============================================================================
import socket
gs0=bytearray(b'\xa1\x00\x00\x00\x55\x03\x08\x01\x00\x09\x00')
gs1=bytearray(b'\xa1\x00\x00\x00\x55\x03\x08\x11\x00\x19\x00')
r00=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x00\x00\x08\x00')
r01=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x10\x00\x00\x18\x00')
r11=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x10\x64\x00\x7c\x00')
r10=bytearray(b'\xa1\x00\x00\x00\x55\x04\x08\x00\x64\x00\x6c\x00')
# B: 102,1    F:107,0
plc = mt.TcpMaster('10.0.0.254', 502)  # modbus
#master = mt.TcpMaster('10.0.0.100', 502)  # modbus

plc_cmd = plc.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS,
                               starting_address=0, quantity_of_x=70)
plc_lis = list(plc_cmd)
def eeye2(s,r1,r2,t):
    while True:
        response = s.recv(1024)
        if '\\xa2' in str(response):
            time.sleep(t)
            s.sendall(r1)
            s.sendall(r2)
            
# =============================================================================
#             time.sleep(3)
#             plc_lis[64]=2  # B stop down
#             plc_lis[66]=1  # D stop up
#             plc_exc(plc_lis)
#             time.sleep(1)
#             s2.sendall(r11)
#             time.sleep(2)
#             plc_lis[52]=1  # E go
#             plc_lis[55]=1  # A go
#             plc_lis[64]=1  # B stop up
#             plc_exc(plc_lis)
# =============================================================================
            return 1
        else:
            s.sendall(gs0)
            return 0
def eeye3(s,r1,r2,t):
    while True:
        response = s.recv(1024)
        if '\\xa2' in str(response):
            time.sleep(t)
            s.sendall(r1)
            s.sendall(r2)
            
# =============================================================================
#             time.sleep(2)
#             s3.sendall(r11)
# =============================================================================
            return 1
        else:
            s.sendall(gs0)
            return 0
def eeye4(s,r1,r2,t):
    while True:
        response = s.recv(1024)
        if '\\xa2' in str(response):
            time.sleep(t)
            s.sendall(r1)
            s.sendall(r2)
            
# =============================================================================
#             plc_lis[60]=1   # D trans up
#             plc_exc(plc_lis)
#             time.sleep(1)
#             plc_lis[59]=1  # D trans go
#             plc_exc(plc_lis)
#             time.sleep(2)
#             plc_lis[59]=0  # D trans stop
#             plc_lis[60]=2  # D trans down
#             plc_exc(plc_lis)
#             s4.sendall(r11)
#             s4.sendall(r10)
# =============================================================================
            return 1
        else:
            s.sendall(gs0)
            return 0
# =============================================================================
# def eeye5(s,r1,r2,t):
#     while True:
#         response = s.recv(1024)
#         if '\\xa2' in str(response):
#             time.sleep(t)
#             s.sendall(r1)
#             s.sendall(r2)
#             return 1
#         else:
#             s.sendall(gs0)
#             return 0
# =============================================================================
def eeye7(s,r1,r2,t):
    while True:
        response = s.recv(1024)
        if '\\xa2' in str(response):
            time.sleep(t)
            s.sendall(r1)
            s.sendall(r2)
            
# =============================================================================
#             time.sleep(3)
#             plc_lis[62]=2  # B stop  down
#             plc_exc(plc_lis)
#             time.sleep(1)
#             s7.sendall(r10)
# =============================================================================
            return 1
        else:
            s.sendall(gs0)
            return 0
def eeye8(s,r1,r2,t):
    while True:
        response = s.recv(1024)
        if '\\xa2' in str(response):
            time.sleep(t)
            s.sendall(r1)
            s.sendall(r2)
            
# =============================================================================
#             time.sleep(4)
#             plc_lis[62]=1  # B stop up
#             plc_exc(plc_lis)
#             s8.sendall(r10)
# =============================================================================
            return 1
        else:
            s.sendall(gs0)
            return 0
def eeye9(s,r1,r2,t):
    while True:
        response = s.recv(1024)
        if '\\xa2' in str(response):
            time.sleep(t)
            s.sendall(r1)
            s.sendall(r2)
            
# =============================================================================
#             plc_lis[56]=0  # G trans stop
#             plc_lis[57]=2  # G trans down
#             plc_exc(plc_lis)
#             time.sleep(2)
#             s9.sendall(r10)
#             s9.sendall(r11)
# =============================================================================
            return 1
        else:
            s.sendall(gs0)
            return 0
def eeye12(s,r1,r2,t):
    while True:
        response = s.recv(1024)
        if '\\xa2' in str(response):
            time.sleep(t)
            s.sendall(r1)
            s.sendall(r2)
            
# =============================================================================
#             plc_lis[56]=1  # G trans go
#             plc_lis[57]=1  # G trans up
#             plc_exc(plc_lis)
#             time.sleep(3)
#             s12.sendall(r11)
# =============================================================================
            return 1
        else:
            s.sendall(gs0)
            return 0

def socketset(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.0.0.{}'.format(ip), 5566))
    return s

def plc_exc(lis):
    plc.execute(1, cst.WRITE_MULTIPLE_REGISTERS,  starting_address=0, output_value=lis)


def k2():
    time.sleep(3)
    plc_lis[52]=1  # E go
    plc_lis[55]=1  # A go
    plc_lis[64]=2  # B stop down
    plc_lis[66]=1  # D stop up
    plc_exc(plc_lis)
    time.sleep(1)
    s2.sendall(r11)
    time.sleep(2)
    plc_lis[64]=1  # B stop up
    plc_exc(plc_lis)
def k3():
    time.sleep(2)
    s3.sendall(r11)
def k4():
    plc_lis[60]=1   # D trans up
    plc_exc(plc_lis)
    time.sleep(1)
    plc_lis[59]=1  # D trans go
    plc_exc(plc_lis)
    time.sleep(2)
    plc_lis[59]=0  # D trans stop
    plc_lis[60]=2  # D trans down
    plc_exc(plc_lis)
    s4.sendall(r11)
    s4.sendall(r10)
def k12():
    plc_lis[56]=1  # G trans go
    plc_lis[57]=1  # G trans up
    plc_exc(plc_lis)
    time.sleep(3)
    s12.sendall(r11)
def k9():
    plc_lis[56]=0  # G trans stop
    plc_lis[57]=2  # G trans down
    plc_exc(plc_lis)
    time.sleep(2)
    s9.sendall(r10)
    s9.sendall(r11)
def k8():
    time.sleep(4)
    plc_lis[62]=1  # B stop up
    plc_exc(plc_lis)
    s8.sendall(r10)
def k7():
    time.sleep(3)
    plc_lis[62]=2  # B stop  down
    plc_exc(plc_lis)
    time.sleep(1)
    s7.sendall(r10)
    
s2 = socketset(102)
s3 = socketset(103)
s4 = socketset(104)
#s5 = socketset(105)
s7 = socketset(107)
s8 = socketset(108)
s9 = socketset(109)
s12 = socketset(112)

plc_lis[50]=1
plc_lis[51]=1
plc_lis[53]=1
plc_lis[54]=1
plc_lis[55]=1
plc_lis[64]=1
plc_exc(plc_lis)

cmd=1
while True:
#    k1 = cc101(s1)
    e2 = eeye2(s2,r01,gs0,0)
    e3 = eeye3(s3,r01,gs0,0)
    e4 = eeye4(s4,r00,r01,2)
#    e5 = eeye5(s5,r01,gs0,0)
    e7 = eeye7(s7,r00,gs0,0)
    e8 = eeye8(s8,r00,gs0,0)
    e9 = eeye9(s9,r00,r01,2)
    e12 = eeye12(s12,r01,gs0,0)
#    k = [k2,k3,k4,k5,k7,k8,k9,k12]

    if e2 :
#        stop = SmartConvey_mian_def(s2)
        # A move on and D stop up
        k2()

    if e3 :
        k3()

    if e4 : # D
        # trans up and stop down
        if plc_lis[66]==1:  # D stop
            k4()

#    if k5:
#        s10.sendall(r00)
    if e12 :
        k12()
    if e9 :
        k9()
    if e8 :
        k8()
    if e7 :
#        SmartConvey_mian_def(s7)
        k7()
    
        

        

if __name__ == '__main__':  #k = [k2,k3,k4,k5,k7,k8,k9,k12]
    p2 = multiprocessing.Process(name='p2', target=eeye2)
    p3 = multiprocessing.Process(name='p3', target=eeye3)
    p4 = multiprocessing.Process(name='p4', target=eeye4)
#    p5 = multiprocessing.Process(name='p5', target=eeye5)
    p7 = multiprocessing.Process(name='p7', target=eeye7)
    p8 = multiprocessing.Process(name='p8', target=eeye8)
    p9 = multiprocessing.Process(name='p9', target=eeye9)
    p12 = multiprocessing.Process(name='p12', target=eeye12)

    pk2= multiprocessing.Process(name='pk2', target=k2)
    pk3= multiprocessing.Process(name='pk3', target=k3)
    pk4= multiprocessing.Process(name='pk4', target=k4)
#    pk5= multiprocessing.Process(name='pk5', target=k5)
    pk7= multiprocessing.Process(name='pk7', target=k7)
    pk8= multiprocessing.Process(name='pk8', target=k8)
    pk9= multiprocessing.Process(name='pk9', target=k9)
    pk12= multiprocessing.Process(name='pk12', target=k12)
    
    p2.start()
    p3.start()
    p4.start()
#    p5.start()
    p7.start()
    p8.start()
    p9.start()
    p12.start()
    
    pk2.start()
    pk3.start()
    pk4.start()
#    pk5.start()
    pk7.start()
    pk8.start()
    pk9.start()
    pk12.start()
    
#    if k10:
#        s5.sendall(r11)
        
        
    ########################################################################    

# =============================================================================
# def add():
#     while True:
#         print (1)
#         time.sleep(3)
# 
# def sud():
#      while True:
#         print(0)
#         time.sleep(3)
# =============================================================================
# =============================================================================
# def cc101(s1):
#     while True:
#         response1 = s1.recv(1024)
#         if '\\xa2' in str(response1):
#             s1.sendall(r00)
#             return 1
#         else:
#             s1.sendall(gs0)
#             return 0
# def cc102(s2):
#     while True:
#         response2 = s2.recv(1024)
#         if '\\xa2' in str(response2):
#             s2.sendall(r01)
#             return 2
#         else:
#             s2.sendall(gs0)
#             return 0
# def cc104(s4):
#     while True:
#         response4 = s4.recv(1024)
#         if '\\xa2' in str(response4):
#             time.sleep(2)
#             s4.sendall(r01)
#             return 4
#         else:
#             s4.sendall(gs0)
#             return 0
# def cc105(s5):
#     while True:
#         response5 = s5.recv(1024)
#         if '\\xa2' in str(response5):
#             s5.sendall(r01)
#             return 5
#         else:
#             s5.sendall(gs0)
#             return 0
# def cc107(s7):
#     while True:
#         response7 = s7.recv(1024)
#         if '\\xa2' in str(response7):
#             s7.sendall(r00)
#             return 7
#         else:
#             s7.sendall(gs0)
#             return 0
# def cc110(s10):
#     while True:
#         response10 = s10.recv(1024)
#         if '\\xa2' in str(response10):
#             time.sleep(2)
#             s10.sendall(r10)   # move on
#             return 10
#         else:
#             s10.sendall(gs0)
#             return 0
# #t1 = threading.Thread(target = cc101)
# #t1.start()
# #t2 = threading.Thread(target = cc102)
# #t2.start()
# 
# s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s1.connect(('10.0.0.101', 5566))
# s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s2.connect(('10.0.0.102', 5566))
# s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s4.connect(('10.0.0.104', 5566))
# s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s5.connect(('10.0.0.105', 5566))
# s7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s7.connect(('10.0.0.107', 5566))
# s10 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s10.connect(('10.0.0.110', 5566))    
# =============================================================================
