from turtle import *

def sq():
    down()
    for i in range (4):        
        fd(10)
        right(90)
    up()

mf = open("test.txt","r")
a = mf.read()
mf.close()

mmap=[]

speed(0)
up()
goto(10, 0)

line = 0
tmp = []
for c in a:
    if c == '#':
        sq()
        tmp.append(1)
    if c == '\n':
        line += 1
        goto(0,(line * (-10)))
        mmap.append(tmp)
        tmp = []
    if c == '0':tmp.append(0)
    forward(10)
#done()
