from GrantHewettgraphicsModifiedForGOB import *
import math
import random
maxX = 800
maxY = 600
win = GraphWin("One Bullet", maxX , maxY, autoflush=False)
win.setBackground("gray")
player= Circle(Point(maxX/2, maxY/2),30)  #if you really want a challenge, make the player size bigger
player.setFill("blue")
player.draw(win)
score = 0  #My highscore is 156
sText = "Score: "
scoreText = Text(Point(.8*maxX,20),sText+ str(score))
scoreText.draw(win)
livesLeft=3
livesText= Text(Point(30,20), "Lives: " + str(livesLeft))
livesText.draw(win)
story= Text(Point(maxX/2, 220),"Story: \n Your ship has been stranded in the middle of an asteroid belt \n It's your job to keep the ship safe \n Good thing you have your handy-dandy Boomerang Bullet")
story.draw(win)
intro = Text(Point(maxX/2, 400), "How To Play: \n Click where you want the bullet to go, and don't let it go off screen \n Try to hit the asteroids coming at you \n Try to collect Power-Ups \n Keep track of your lives and try to get a highscore\nClick to Start")
intro.draw(win)
win.getMouse()
story.undraw()
intro.undraw()
clickLoc = win.checkMouse()
if clickLoc != None:  #clickLoc either returns the point clicked or None, constantly
    delX,delY = clickLoc.getUnitVectorToward(player.getCenter())
asteroids=[]
laser = Circle(Point(maxX / 2, maxY / 2), 4)
laser.setOutline("blue")  # makes laser look invisible
laser.draw(win)
faster= Circle(Point(random.randint(-5000,-2500),random.randint(60,500)),20)
faster.setFill("firebrick")
faster.draw(win)
fcounter=0
fcount=False
bigger= Circle(Point(random.randint(-2000,-500),random.randint(60,500)),20)
bigger.setFill("darkgreen")
bigger.draw(win)
bcounter=0
bcount=False
n=35  #Number of astriods, gets really laggy after 50(depends on the computer)
for x in range(n):
    #Mess around with x-cor and radius for higher or lower difficulty
    asteroid = Circle(Point(random.randint(-3000,-35),random.randint(70,500)),random.randint(25,50))
    asteroid.setFill("slategrey")
    asteroid.draw(win)
    asteroids.append(asteroid)
shoot=False
counter=0
speed=4.3
t1 = Text(Point(maxX / 2, 350), "You Lose!! \n Click to Play Again")
t2 = Text(Point(maxX / 2, 350), "You Win!!  \n Click to Play Again")
while True:
    if counter==1:
        bigger.move(3,0)
        faster.move(3,0)
        counter=0
    if laser.overlaps(bigger) and fcount==False:  #The fcount==False makes it so you can only get one power=up at a time
        laser.undraw()
        laser=Circle(laser.getCenter(),30)
        laser.setOutline("darkgreen")
        laser.draw(win)
        bigger.undraw()
        update()
        bcount=True
    if bcount:
        bcounter+=1
    if bcounter==500:
        bcounter=0
        laser.undraw()
        laser = Circle(laser.getCenter(), 4)
        laser.setOutline("blue")
        laser.draw(win)
        bcount=False
        update()
        bigger = Circle(Point(random.randint(-5000, -3000), random.randint(60, 500)), 20)
        bigger.setFill("darkgreen")
        bigger.draw(win)
        update()
    if bigger.getCenter().getX()>=800:
        bigger.undraw()
        update()
        bigger = Circle(Point(random.randint(-5000, -3000), random.randint(60, 500)), 20)
        bigger.setFill("darkgreen")
        bigger.draw(win)
        update()
    if laser.overlaps(faster) and bcount==False: #The bcount==False makes it so you can only get one power=up at a time
        speed=6.5
        laser.undraw()
        laser = Circle(laser.getCenter(), 4)
        laser.setOutline("firebrick")
        laser.draw(win)
        faster.undraw()
        update()
        fcount=True
        faster = Circle(Point(random.randint(-7000, -5000), random.randint(60, 500)), 20)
        faster.setFill("firebrick")
        faster.draw(win)
        update()
    if fcount:
        fcounter+=1
    if fcounter==500:
        fcounter=0
        laser.undraw()
        laser = Circle(laser.getCenter(), 4)
        laser.setOutline("blue")
        laser.draw(win)
        update()
        fcount=False
        speed=4.3
    if faster.getCenter().getX()>= 800:
        faster.undraw()
        update()
        faster = Circle(Point(random.randint(-5000, -2500), random.randint(60, 500)), 20)
        faster.setFill("firebrick")
        faster.draw(win)
        update()
    point2 = laser.getCenter()
    if livesLeft <= 0 or len(asteroids)==0 or point2.getX() >= 800 or point2.getX() <= 0 or point2.getY() >= 600 or point2.getY() <= 0:
        if livesLeft ==0 or point2.getX() >= 800 or point2.getX() <= 0 or point2.getY() >= 600 or point2.getY() <= 0:
            t1.draw(win)
            update()
            win.getMouse()
            t1.undraw()
        if len(asteroids)==0:
            t2.draw(win)
            update()
            win.getMouse()
            t2.undraw()
        bigger.undraw()
        faster.undraw()
        speed=4.3
        livesLeft=3
        score=0
        scoreText.setText(sText + str(score))
        livesText.setText("Lives: " + str(livesLeft))
        laser.undraw()
        update()
        laser = Circle(Point(maxX / 2, maxY / 2), 4)
        laser.setOutline("blue")  # makes laser look invisible
        laser.draw(win)
        update()
        for x in asteroids:
            x.undraw()
            update()
        asteroids=[]
        for y in range(n):
            # Mess around with x-cor and radius for higher or lower difficulty
            asteroid = Circle(Point(random.randint(-3000, -35), random.randint(70, 500)), random.randint(25, 50))
            asteroid.setFill("slategrey")
            asteroid.draw(win)
            asteroids.append(asteroid)
        bigger = Circle(Point(random.randint(-2000,-500), random.randint(60, 500)), 20)
        bigger.setFill("darkgreen")
        bigger.draw(win)
        bcount=False
        faster = Circle(Point(random.randint(-5000,-2500), random.randint(60, 500)), 20)
        faster.setFill("firebrick")
        faster.draw(win)
        fcount=False
        intro.draw(win)
        story.draw(win)
        win.getMouse()
        story.undraw()
        intro.undraw()
        update()
    for y,x in enumerate(asteroids):
        point3 = x.getCenter()
        if point3.getX() >= 800:
            asteroids[y].undraw()
            asteroids[y]= Circle(Point(random.randint(-2000,-35),random.randint(70,500)),random.randint(25,50))
            asteroids[y].setFill("slategrey")
            asteroids[y].draw(win)
            update()
        asteroids[y].move(random.randint(2, 5),0)
        if x.overlaps(player) or laser.overlaps(x):
            asteroids.pop(y)
            newAsteriod=Circle(Point(random.randint(-2000,-35),random.randint(70,500)),random.randint(25,50))
            newAsteriod.setFill("slategray")
            newAsteriod.draw(win)
            asteroids.append(newAsteriod)
        if x.overlaps(player):
            x.undraw()
            livesLeft-=1
            livesText.setText("Lives: " + str(livesLeft))
            player.undraw()
            update()
            time.sleep(.1)
            player.draw(win)
            update()
            time.sleep(.1)
            player.undraw()
            update()
            time.sleep(.1)
            player.draw(win)
            update()
        if laser.overlaps(x):
            x.undraw()
            update()
            score+=1
            scoreText.setText(sText + str(score))
            update()
    clickLoc = win.checkMouse()
    if clickLoc != None:
        delX, delY = clickLoc.getUnitVectorToward(laser.getCenter())
        delX, delY = delX*speed, delY*speed
        shoot=True
        clickLoc1=clickLoc  #To make clickLoc equal to a point instead of None
    if clickLoc != None or shoot==True:
        if clickLoc1.getDistance(player.getCenter())>1:
            #move toward clickLoc
            laser.move(delX, delY)
        else: #wait for the next click location
            clickLoc = win.getMouse()
            delX, delY = clickLoc.getUnitVectorToward(player.getCenter())
    counter+=1
    time.sleep(.01)
    update()