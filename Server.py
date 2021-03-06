from turtle import *
import socket

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
    StartPoint = []
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
                Destination = [i,j]
                #print destination
            if map_list [j][i] == '@':            
                color("yellow")
                begin_fill()
                DrawSquare()
                end_fill()
                fd(15)
                color("black")
                StartPoint = [i,j]    
                #print start_point
        goto(-375, (j+1) * -15 + 225)
    return StartPoint, map_list

StartPoint, map_list = DrawMap()

up()
goto (StartPoint[0] * 15 - 375, StartPoint[1] * -15 + 225)
down()
color('green')

print("Darwing done, waiting for a client to join")

#host = '172.17.8.83'
host = ''
port = 50001
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data == '<Salamon alaikom va rahmatollahe va barakatoh!>':
        print 'a client has joined'
        client.send('<Alaikom ossalam>')
        break

currentPlace = [0,0]
currentPlace[0] = StartPoint[0]
currentPlace[1] = StartPoint[1]
NumRahnama = 0
Moves = 0
InvalidMoves = 0
Reached = False



while 1:
    data = client.recv(size)
    print data
    if data == '<Rahnama!>':
        respond = []
        respond.append(0 if map_list[currentPlace[1]][currentPlace[0]-1]== ' ' 
            or map_list[currentPlace[1]][currentPlace[0]-1] == '&'
            or map_list[currentPlace[1]][currentPlace[0]-1] == '@' else 1)

        respond.append(0 if map_list[currentPlace[1]-1][currentPlace[0]]== ' ' 
            or map_list[currentPlace[1]-1][currentPlace[0]] == '&'
            or map_list[currentPlace[1]-1][currentPlace[0]] == '@' else 1)

        respond.append(0 if map_list[currentPlace[1]][currentPlace[0]+1]== ' ' 
            or map_list[currentPlace[1]][currentPlace[0]+1] == '&'
            or map_list[currentPlace[1]][currentPlace[0]+1] == '@' else 1)

        respond.append(0 if map_list[currentPlace[1]+1][currentPlace[0]]== ' ' 
            or map_list[currentPlace[1]+1][currentPlace[0]] == '&' 
            or map_list[currentPlace[1]+1][currentPlace[0]] == '@' else 1)

        client.send('<'+str(respond)+'>')

        NumRahnama += 1
        #else: s.shutdown(1)
    else:
        if data == '<LEFT>':
            if map_list[currentPlace[1]][currentPlace[0]-1]== 'x':
                client.send('<Invalid Move!>')
                InvalidMoves += 1
            elif map_list[currentPlace[1]][currentPlace[0]-1]== '&':
                Reached = True
                Moves += 1
                client.send('<Congrats!>')
                currentPlace[1] -= 1
                break
            else:
                client.send('<Halle!>')
                Moves += 1
                currentPlace[0] -= 1
                #left(180-heading())
        if data == '<RIGHT>':
            if map_list[currentPlace[1]][currentPlace[0]+1]== 'x':
                client.send('<Invalid Move!>')
                InvalidMoves += 1
            elif map_list[currentPlace[1]][currentPlace[0]+1]== '&':
                Reached = True
                Moves += 1
                client.send('<Congrats!>')
                currentPlace[1] += 1
                break
            else:
                client.send('<Halle!>')
                Moves += 1
                currentPlace[0] += 1
                #left(0-heading())
        if data == '<UP>':
            if map_list[currentPlace[1]-1][currentPlace[0]]== 'x':
                client.send('<Invalid Move!>')
                InvalidMoves += 1
            elif map_list[currentPlace[1]-1][currentPlace[0]]== '&':
                Reached = True
                Moves += 1
                client.send('<Congrats!>')
                currentPlace[0] -= 1
                break
            else:
                client.send('<Halle!>')
                Moves += 1
                currentPlace[1] -= 1
                #left(90-heading())
        if data == '<DOWN>':
            if map_list[currentPlace[1]+1][currentPlace[0]]== 'x':
                client.send('<Invalid Move!>')
                InvalidMoves += 1
            elif map_list[currentPlace[1]+1][currentPlace[0]]== '&':
                Reached = True
                Moves += 1
                client.send('<Congrats!>')
                currentPlace[0] += 1
                break
            else:
                client.send('<Halle!>')
                Moves += 1
                currentPlace[1] += 1
                #left(270-heading())
        else:
            client.send('<Invalid Move!>')
            InvalidMoves += 1
        goto (currentPlace[0] * 15 - 375, currentPlace[1] * -15 + 225)
        begin_fill()
        DrawSquare()    
        end_fill()
#    goto (currentPlace[0] * 15 - 375, currentPlace[1] * -15 + 225)

s.shutdown()
print "total moves: ", Moves
print 'total Invalid Moves: ', InvalidMoves
print 'number of rahnamas!: ', NumRahnama
raw_input()