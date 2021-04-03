from Graphics import *
import random
win = GraphWin("Animation",800,600)
myCircles=[]
colors=["red","purple", "green","white","blue","orange","yellow","Turquoise","Cyan", "Cadet Blue"]
for i in range(150):
    r=random.randint(5,50)
    x= random.randint(0,800)
    y=random.randint(0,600)
    z = Circle(Point(x,y),r)
    z.setFill(random.choice(colors))
    z.draw(win)
    myCircles.append(z)
while True:
    for c in myCircles:
        c.move(random.randint(-2,2),random.randint(-2,2))
        c.setFill(random.choice(colors))
    time.sleep(.0001)
    update()