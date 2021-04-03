#print "1"
#num=0
#while num==0:
 #   num=int(input("Number: "))
#print "The number of eggs is", num/144,"gross, ", (num%144)/12, "dozen, and", ((num%144)%12)

#print "2"
import random
#letter=0
#while letter != "exit":
 #   y = random.randint(1, 6)
  #  x = random.randint(1, 6)
   # letter = raw_input("Type 'r' to roll, 'exit' to end: ")
    #if letter =="r":
     #   print "The first die comes up", x
      #  print "The second die comes up", y
       # print"Your total roll is", x+y
    #if letter == "exit":
     #   counter=1

#print"3"
#change=0
#while change==0:
 #   change=raw_input("How much change do you have? ")
  #  list1=change.split(",")
   # list1=map(int,list1)
#print list1[0], "quarters, ", list1[1], "dimes, ", list1[2], "nickels and", list1[3], "pennies = $",
#print (list1[0]*.25 + list1[1]*.10 + list1[2]*.05 +list1[3]*.01)

print "4"
import time
letter=0
ctotal=0
ptotal=0
pwins=0
cwins=0
while letter != "exit":
    y = random.randint(1, 6)
    x = random.randint(1, 6)
    letter = raw_input("Try to get as close to 21 as you can without going over, type 'go' to start a new game, type 'r' to roll, 's' to stay, and type 'exit' to exit: ")
    if letter =="go":
        print "Player: The first die comes up", x
        print "Player: The second die comes up", y
        print"Player: Your total roll is", x+y
        ptotal=x+y
    if letter=="r":
        y = random.randint(1, 6)
        x = random.randint(1, 6)
        print "Player: The first die comes up", x
        print "Player: The second die comes up", y
        print"Player: Your total roll is", ptotal+x + y
        ptotal = ptotal+x + y
    if letter == "s" or ptotal>21:
        y = random.randint(1, 6)
        x = random.randint(1, 6)
        print "Computer: The first die comes up", x
        print "Computer: The second die comes up", y
        print"Computer: Your total roll is", x + y
        ctotal = x + y
        time.sleep(2)
        if ptotal>21:
            while ctotal <15:
                y = random.randint(1, 6)
                x = random.randint(1, 6)
                print "Computer: The first die comes up", x
                print "Computer: The second die comes up", y
                print"Computer: Your total roll is", ctotal+x+y
                ctotal = ctotal + y + x
                time.sleep(1)
        if ptotal<=21:
            while ctotal <ptotal:
                y = random.randint(1, 6)
                x = random.randint(1, 6)
                print "Computer: The first die comes up", x
                print "Computer: The second die comes up", y
                print"Computer: Your total roll is", ctotal+x+y
                ctotal= ctotal + y + x
                time.sleep(1)
        if ptotal>ctotal and ptotal<=21 or ctotal>21:
            pwins= pwins+1
            print "You Win"
        if ctotal>=ptotal and ctotal<=21 or ptotal>21:
            cwins= cwins+1
            print "Computer Win"
print "computer wins:",cwins
print "player wins:", pwins
