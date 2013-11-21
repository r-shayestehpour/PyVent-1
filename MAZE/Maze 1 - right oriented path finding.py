#################################################   imports
from turtle import *
import time

#################################################   functions
def sq():
    '''draws a square'''
    down()
    for i in range (4):        
        fd(10)
        right(90)
    up()

def adj(map_list, point, h):
    '''returns the front and the right adjacent of point, in the list map_list'''
    rght = bool()
    frwrd = bool()
    if h == 0:
        #print map_list [point[1]][point[0] + 1], map_list [point[1] + 1][point[0]]
        if map_list [point[1]][point[0] + 1] == '0': frwrd = True
        else: frwrd = False
        if map_list [point[1] + 1][point[0]] == '0': rght = True
        else: False
    if h == 90:
        #print map_list [point[1] - 1][point[0]], map_list [point[1]][point[0] + 1]
        if map_list [point[1] - 1][point[0]] == '0' or map_list [point[1] - 1][point[0]] == '*':frwrd = True
        else: False
        #print frwrd
        if map_list [point[1]][point[0] + 1] == '0' or map_list [point[1]][point[0] + 1] == '*':rght = True
        else: False
    if h == 180:
        if map_list [point[1]][point[0] - 1] == '0' or map_list [point[1]][point[0] - 1] == '*':frwrd = True
        else: False
        if map_list [point[1] - 1][point[0]] == '0' or map_list [point[1] - 1][point[0]] == '*':rght = True
        else: False
    if h == 270:
        if map_list [point[1] + 1][point[0]] == '0' or map_list [point[1] + 1][point[0]] == '*':frwrd = True
        else: False
        if map_list [point[1]][point[0] - 1] == '0' or map_list [point[1]][point[0] - 1] == '*':rght = True
        else: False
    #raw_input()
    #time.sleep(0.2)
    return frwrd, rght

def set_direction(map_list, point, h):
    '''returns heading for the turtle according to the func adj'''
    frwrd , rght = adj(map_list, point, h)
    if frwrd and rght: return 'r'
    if not frwrd and rght: return 'r'
    if frwrd and not rght: return 'f'
    else: return 'l'

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
for j in range (len ( map_list ) ):
    for i in range (len (map_list[j] )):
        if map_list [j][i] == '#':
            sq()
            fd(10)
        if map_list [j][i] == '0':
            fd(10)
        if map_list [j][i] == '*':
            color("blue")
            begin_fill()
            sq()
            end_fill()
            color("black")
            destination = [i, j]
            #print destination
        if map_list [j][i] == '@':            
            color("yellow")
            begin_fill()
            sq()
            end_fill()
            color("black")
            start_point = [i, j]
            #print start_point
    goto(0, (j+1) * -10)

#@@@@@@@    right oriented path finding
speed(1)
goto (start_point[0] * 10, start_point[1] * -10)
down()
color('green')
current_point = start_point
setheading(0)
while current_point != destination:
    if set_direction(map_list, current_point, heading()) == 'r':
        #print 'r'
        if heading() == 0 :
            current_point = [current_point[0], current_point[1] + 1]
            right (90)
            fd (10)
        elif heading() == 90 :
            current_point = [current_point[0] + 1, current_point[1]]
            right (90)
            fd (10)
        elif heading() == 180 :
            current_point = [current_point[0], current_point[1] - 1]
            right (90)
            fd (10)
        elif heading() == 270 :
            current_point = [current_point[0] - 1, current_point[1]]
            right (90)
            fd (10)
    elif set_direction(map_list, current_point, heading()) == 'f':
        #print 'f'
        if heading() == 0 :
            current_point = [current_point[0] + 1, current_point[1]]
            fd (10)
        elif heading() == 90 :
            current_point = [current_point[0], current_point[1] - 1]
            fd (10)
        elif heading() == 180 :
            current_point = [current_point[0] - 1, current_point[1]]
            fd (10)            
        elif heading() == 270 :
            current_point = [current_point[0], current_point[1] + 1]
            fd (10)
    elif set_direction(map_list, current_point, heading()) == 'l':
        #print 'l'
        left(90)
a=input()
