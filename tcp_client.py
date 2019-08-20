# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 13:07:04 2019

@author: Sunny
"""
'''
import socket
#hostname = '127.0.0.1'
#port = 7777
#addr = (hostname,port)
#clientsock = socket.socket() ## 建立一個socket
#clientsock.connect(addr) # 建立連線
def main():
    while True:
        clientsock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsock.connect((socket.gethostname(),1234))
        say = input("Type something：")
        clientsock.send(bytes(say,encoding='gbk')) #傳送訊息
        recvdata = clientsock.recv(1024)  #接收訊息 recvdata 是bytes形式的
        print(str(recvdata,encoding='gbk')) # 我們看不懂bytes，所以轉化為 str
        if say =='q' or 'exit':
            break
    clientsock.close()
    
if __name__=='__main__':
    main()
'''
    
    
    
import select
import socket

HOST = '10.0.0.102'
PORT = 5566
timeout = 60 * 1   # 1 分钟

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('msg')
# 设置 recv 超时时间
s.setblocking(0)
ready = select.select([s], [], [], timeout)
if ready[0]:
    # 接收结果
    data = s.recv(1024).strip('\x00')
    print(data,repr(data))