#!/usr/bin/env python

"""
A simple echo client
"""

import socket

host = 'localhost'
port = 50002
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

s.send('#hs')
print '#hs'

print 'type " >Exit< " to end the conversation'

while 1:
    #you = str()
    data = s.recv(size)
    if data == '>s,exit<':
        if str(raw_input('client has quited, want to continue?[y/n]')) == 'y': continue
        else: s.shutdown(1) 
    if data : print 'server says: ', data
    you = str(raw_input('you: '))
    if you == '>Exit<' :
        s.send('>c,exit<')
        s.shutdown(1)
    if you:
        s.send(you)
    

