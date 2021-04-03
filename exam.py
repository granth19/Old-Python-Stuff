print "1"
sum=6200000000
year= 2002
print "Year", "Population"
while sum <= 10110967214.4:
    print year, sum
    year = year + 1
    sum= sum + 0.012*sum
print"2"
num=0
price=0
while num==0:
    num= int(input("Enter number of copies: "))
    if num<=100:
        price= .05*num
    if 500>num>100:
        price = 5 + (num-100)*.03
    if num>=500:
        price= (5+ (num-100)*.03)
        price= price- price*.07
print "Your price is: $", price