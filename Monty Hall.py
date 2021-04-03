import turtle
door=[turtle.Turtle() for t in range(3)]
loc=-250
for x in range(len(door)):
    door[x].speed(100)
    door[x].penup()
    door[x].setpos(loc, -200)
    door[x].setheading(90)
    door[x].pendown()
    loc = loc + 200
for x in range(len(door)):
    for y in range(2):
        door[x].forward(300)
        door[x].right(90)
        door[x].forward(150)
        door[x].right(90)
for x in range(len(door)):
    door[x].penup()
    door[x].forward(150)
    door[x].right(90)
    door[x].forward(75)
    door[x].setheading(90)
    door[x].pendown()
    door[x].write(x+1)
import random
car = random.randint(1, 3)
doors = [1, 2, 3]
choice = int(input("Choose a Door(1-3):"))
if car == choice:
    doors.remove(car)
    r = doors[random.randint(0,1)]
else:
    if car == 3 or choice == 3:
        r = abs(car - choice)
    else:
        r = 3
print "Door #", r, "has a goat behind it"

ss = raw_input("Do you want to switch or stay:")
if ss == "stay" and choice == car:
    print "You Win a car"
if ss == "stay" and choice != car:
    print "You Win a goat"
if ss == "switch" and choice == car:
    print "You Win a goat"
if ss == "switch" and choice != car:
    print "You Win a car"

win = turtle.Screen()
win.exitonclick()