import random
print "1"
sims=1000000
total=0.0
for x in range(sims):
    if random.randint(1,6)==1 and random.randint(1,13)==1:
        total=total+1
print (total/sims)*100, "%"
print "2"
total2=0.0
for x in range(sims):
    if random.randint(1,6)==4 and random.randint(1,6)==4 and random.randint(1,6)==4 and random.randint(1,6)==4:
        total2=total2+1
print (total2/sims)*100, "%"
print "3"
total3=0.0
for x in range(sims):
    if (random.randint(1,6)+random.randint(1,6))%2==0 and random.randint(1,2)==1:
        total3=total3+1
print (total3/sims)*100, "%"
print"4"
total4=0.0
for x in range(sims):
    if random.randint(1,2)==1 and random.randint(1,2)==1 and random.randint(1,2)==1 and random.randint(1,2)==1 and random.randint(1,2)==1:
        total4=total4+1
print (total4/sims)*100, "%"
print "5"
total5=0.0
for x in range(sims):
    deck = random.randint(1,51)
    if deck==1 or deck==2 or deck==3:
        total5=total5+1
print (total5/sims)*100, "%"
total7=0.0
for x in range(sims):
    deck=range(1,53)
    card=random.randint(0,51)
    deck.remove(deck[card])
    if (random.choice(deck))/4==card/4:
        total7=total7+1
print (total7/sims)*100, "%"
print "6"
total6=0.0
for x in range(sims):
    if random.randint(1,2)==1 and random.randint(1,203)==1:
        total6=total6+1
print (total6/sims)*100,"%"