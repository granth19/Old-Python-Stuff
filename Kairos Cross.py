import turtle
t= turtle.Turtle()
t.speed(30)
def T():
    for x in range(4):
        t.forward(80)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(15)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(80)
        t.left(90)
def Cross():
    for x in range(4):
        t.forward(35)
        t.left(90)
        t.forward(35)
        t.right(90)
        t.forward(10)
        t.right(90)
T()
t.forward(35)
t.left(90)
Cross()
t.left(90)
t.penup()
t.forward(120)
t.pendown()
t.right(90)
Cross()
t.right(90)
t.forward(10)
t.right(90)
t.penup()
t.forward(40)
t.pendown()
Cross()
t.left(90)
t.penup()
t.forward(120)
t.pendown()
t.right(90)
Cross()

win = turtle.Screen()
win.exitonclick()