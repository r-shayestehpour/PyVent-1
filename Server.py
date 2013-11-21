from turtle import *
import socket

Destination = tuple
StartPoint = tuple

def DrawSquare():
    '''draws a square'''
    down()
    for i in range (4):        
        fd(15)
        right(90)
    up()

def DrawMap():
    '''Draws the map'''
    mf = open("map.txt","r")
    map_list = mf.readlines()
    mf.close()

    speed(0)
    delay(0)
    up()
    goto (-375, 225)
    raw_input("Loaded map, Start Drawing? [y/n]")
    for j in range (len ( map_list ) ):
        for i in range (len (map_list[j] )):
            if map_list [j][i] == 'x':
                DrawSquare()
                fd(15)
            if map_list [j][i] == ' ':
                fd(15)
            if map_list [j][i] == '&':
                color("blue")
                begin_fill()
                DrawSquare()
                end_fill()
                fd(15)
                color("black")
                Destination = (i,j)
                #print destination
            if map_list [j][i] == '@':            
                color("yellow")
                begin_fill()
                DrawSquare()
                end_fill()
                fd(15)
                color("black")
                StartPoint = (i,j)    
                #print start_point
        goto(-375, (j+1) * -15 + 225)

DrawMap()

raw_input("Darwing done, waiting for a client to join")

host = ''
port = 50002
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data == '<Salamon alaikom va rahmatollahe va barakatoh!>':
        print 'a client has joined'
        break

