class Vehicle:
    def __init__(self,sp):
        self.wheels = 4
        self.speed = sp

    def accelerate(self,value):
        self.speed+=value

    def __str__(self):
        return "A vehicle with " + str(self.wheels) + " wheels."

    def stop(self):
        temp = self.speed
        self.speed = 0
        return -temp

class Car(Vehicle):
    def __init__(self, sp):
        Vehicle.__init__(self,sp)

    def __str__(self):
        return "A car going " + str(self.speed) + " mph."

class Motorcycle(Vehicle):
    def __init__(self,sp):
        Vehicle.__init__(self,sp)
        self.wheels = 2

    def wheelie(self):
        print "Yeehaw!!"

class Truck(Vehicle):
    def __init__(self,sp,pl,cap):
        Vehicle.__init__(self,sp)
        self.payload=pl
        self.capacity=cap

    def __str__(self):
        return "A Truck with a capacity of " + str(self.capacity) + " and a payload of " + str(self.payload)

    def load(self,amount):
        if amount + self.payload <= self.capacity:
            self.payload += amount
            return self.payload
        else:
            return -1

    def dump(self,amount):
        if amount <= self.payload:
            self.payload-=amount
            return self.payload
        else:
            return -1
'''
c1 = Car(10)
#Car.accelerate(c1,-4)
c1.accelerate(-4)
print c1

m1 = Motorcycle(30)
m1.accelerate(5)
print m1
print m1.speed
m1.wheelie()

print c1.stop()
print c1.speed
'''
t1=Truck(20,200,500)
print t1
print t1.load(100)
print t1
print t1.dump(100)
print t1
print t1.load(500)
print t1.dump(500)