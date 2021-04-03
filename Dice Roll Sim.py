import random
import turtle
def roll():
    d1 = random.randint(1,6)
    #d2 = random.randint(1,6)
    #return d1+d2
    return d1

myTurtles = [turtle.Turtle() for t in range(7)]
yStart = -200

def setup():
    loc = -100.0
    for i in range(len(myTurtles)):
        myTurtles[i].speed(30)
        myTurtles[i].penup()
        myTurtles[i].setpos(loc,yStart)
        myTurtles[i].setheading(90)
        myTurtles[i].pendown()
        myTurtles[i].write(i)
        loc+=30

setup()
#for i in range(1000):
 #   myTurtles[roll()].forward(1)
roll2=True
while roll2:
    cord = roll()
    myTurtles[cord].forward(1)
    print myTurtles[cord].ycor()
    if (myTurtles[cord].ycor())==-100:
        roll2=False

for t in myTurtles:
    t.write(t.ycor()+200)

win = turtle.Screen()
win.exitonclick()
