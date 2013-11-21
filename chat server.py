#!/usr/bin/env python

"""
A simple echo server
"""

import socket

host = ''
port = 50002
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

print 'waiting for clients to connect...'
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data == '#hs':
        print '#hs'
        break

print 'type " >Exit< " to end the conversation'

while 1:
    #you = str()
    you = str(raw_input('you: '))
    if you == '>Exit<':
        client.send('>s,exit<')
        client.close()
        s.shutdown(1)
    if you:
        #print 'you say: ', you
        client.send(you)
    data = client.recv(size)
    if data == '>c,exit<':
        if str(raw_input('client has quited, want to continue?[y/n]')) == 'y': continue
        else: s.shutdown(1)
    if data : print 'client says: ', data
