from GrantHewettgraphicsModifiedForGOB import *
import math
import random
maxX = 800
maxY = 600
win = GraphWin("GOB!!!", maxX , maxY, autoflush=False)

#set up game
myColors = ["green","blue","teal"]
score = 0
sText = "Score: "
scoreText = Text(Point(.8*maxX,20),sText+ str(score))
player = Circle(Point(maxX/2, maxY/2), 20)
player.setFill("red")
numCircles = 50
myCircles = []

#draw all the target circles
for i in range(numCircles):
    x = random.randint(0, maxX)
    y = random.randint(0, maxY)
    z = Circle(Point(x, y), random.randint(5,30))
    chosenColor = random.choice(myColors)
    z.setFill(chosenColor)
    z.draw(win)
    myCircles.append(z)

scoreText.draw(win)
player.draw(win)
#play starts here
#get location that was clicked
clickLoc = win.getMouse()
#get x and y values to move
delX,delY = clickLoc.getUnitVectorToward(player.getCenter())
#start animating
while True:
    #if we are greater than 1 px away from target distance
    if clickLoc.getDistance(player.getCenter())>1:
        #move toward clickLoc
        player.move(delX, delY)
        #check for overlaps with all circles
        for c in myCircles:
            if player.overlaps(c):
                score+=1
                scoreText.setText(sText+ str(score))
                c.undraw()
                myCircles.remove(c)
    else: #wait for the next click location
        clickLoc = win.getMouse()
        delX, delY = clickLoc.getUnitVectorToward(player.getCenter())
    time.sleep(.01)
    update()

win.getMouse()
win.close()