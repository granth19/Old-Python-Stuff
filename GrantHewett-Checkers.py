from GrantHewettgraphicsModifiedForGOB import *
import math
import random
maxX = 800
maxY = 700
win = GraphWin("Checkers", maxX , maxY, autoflush=False)
board=[]
x = 50
y = -80
x2 = 130
y2 = 0
row=1
redPieces=[]
rx=170
ry=440
rrow=1
checkered=1
for i in range(64):
    if row%8==1:
        x=50
        x2=130
        y+=80
        y2+=80
    checkered+=1
    square=Rectangle(Point(x,y),Point(x2,y2))
    if checkered%2==1:
        square.setFill("black")
    if row%16==8:
        checkered = 2
    if row%16==0:
        checkered = 1
    square.draw(win)
    board.append(square)
    row+=1
    x+=80
    x2+=80
for i in range(12):
    rPiece=Circle(Point(rx,ry),35)
    rPiece.setFill("firebrick")
    rPiece.draw(win)
    redPieces.append(rPiece)
    rx+=160
    rrow+=1
    if rrow==5:
        rx=90
        ry=520
    if rrow==9:
        rx=170
        ry=600
while True:
    for i in redPieces:
        if i.getCenter().getDistance(win.getMouse())<=35.0:
            movingPiece=i
            print 1
