import random
aver=0
sims=10000
for x in range(sims):
  total=0
  bday=[False for y in range(365)]
  days=True
  while days:
    num=random.randint(0,364)
    if bday[num]:
        days=False
    else:
        bday[num]=True
  for y in bday:
    if y:
        total=total+1
  aver=total+aver
print aver/sims