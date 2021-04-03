from GraphicsModified import *
import math
import random
win = GraphWin("Update Example", 800 , 600, autoflush=False)


def createCircle():
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    z = Circle(Point(x, y), random.randint(5,30))
    return z

c1 = Circle(Point(300,375),random.randint(20,30))
c2 = Circle(Point(500,410),random.randint(20,30))
c1.draw(win)
c2.draw(win)
t1= Text(c1.getCenter(),c1)
while not c1.overlap(c2):
    t1.draw(win)
    c1.move(1,0)
    time.sleep(.01)
    update()
    t1.undraw()
win.getMouse()
win.close()