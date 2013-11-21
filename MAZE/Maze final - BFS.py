#################################################   imports
from turtle import *
#import time
#import copy

#################################################   functions
def sq():
    '''draws a square'''
    down()
    for i in range (4):        
        fd(10)
        right(90)
    up()

#################################################   classes
class node:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = 'white'
        self.dist = 100000000
        self.p =  None
        self.adj = []


#################################################   main body

#@@@@@@@    reading map
mf = open("map.txt","r")
map_list = mf.readlines()
mf.close()

#@@@@@@@    initialising turtle
speed(0)
delay(0)
up()
goto (0, 0)

#@@@@@@@    drawing map
nodes = []
for j in range (len ( map_list ) ):
    for i in range (len (map_list[j] )):
        if map_list [j][i] == 'x':
            sq()
            fd(10)
        if map_list [j][i] == ' ':
            tmp_node = node()
            tmp_node.x = i
            tmp_node.y = j
            nodes.append(tmp_node)
            fd(10)
        if map_list [j][i] == '&':
            color("blue")
            begin_fill()
            sq()
            end_fill()
            color("black")
            tmp_node = node()
            tmp_node.x = i
            tmp_node.y = j
            nodes.append(tmp_node)
            destination = tmp_node
            #print destination
        if map_list [j][i] == '@':            
            color("yellow")
            begin_fill()
            sq()
            end_fill()
            color("black")
            tmp_node = node()
            tmp_node.x = i
            tmp_node.y = j
            nodes.append(tmp_node)
            start_point = tmp_node
            #print start_point
    goto(0, (j+1) * -10)

#################################################    BFS for path finding

#@@@@@@@    building the  adjacency list for vertices
for n in nodes:
    tmp_node = node()
    tmp_node.x = n.x - 1
    tmp_node.y = n.y
    for i in nodes:
        if tmp_node.x == i.x and tmp_node.y == i.y : n.adj.append(i)
    tmp_node.x = n.x + 1
    tmp_node.y = n.y
    for i in nodes:
        if tmp_node.x == i.x and tmp_node.y == i.y : n.adj.append(i)
    tmp_node.x = n.x 
    tmp_node.y = n.y + 1
    for i in nodes:
        if tmp_node.x == i.x and tmp_node.y == i.y : n.adj.append(i)
    tmp_node.x = n.x 
    tmp_node.y = n.y - 1
    for i in nodes:
        if tmp_node.x == i.x and tmp_node.y == i.y : n.adj.append(i)
    #for i in n.adj: print 'a',
    #print '\n'

#@@@@@@@    BFS(G, s)
queue = []

destination.color = 'gray'
destination.dist = 0
queue.append(destination)

while len(queue):
    u = queue[0]
    queue = queue[1:]
    #print u.adj
    for v in u.adj:
        #print 'v'
        if v.color == 'white':
            v.color = 'gray'
            v.dist = u.dist + 1
            v.p = u            
            queue.append (v)
    u.color = 'black'

#@@@@@@@    drawing the path
up()
print start_point.x,start_point.y
goto (start_point.x * 10, start_point.y * -10)
down()
color('green')
tmp = start_point
delay(50)
while tmp != destination:
    #print tmp.p
    tmp = tmp.p
    #print type(tmp)
    goto(tmp.x * 10, tmp.y * -10)

input(":D")
