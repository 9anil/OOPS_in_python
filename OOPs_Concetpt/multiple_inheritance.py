''' Multiple inheritance- A derived class inherits multiple or more than one base class attributes

'''

class car:
    def __init__(self,gears,seats,maxspeed):
        self.gear=gears
        self.seat=seats
        self.maxspeed=maxspeed
    def speedup(self):
        print("Increasing speed")
    def apply_break(self):
        print("Decreasing speed")
    def movement(self):
        print("Moving forward and backward")
class hyundai:
    def __init__(self):
        self.brandname="Hyundai"
class hyundai_india:
    def __init__(self,city):
        self.city=city
class volvo(car):
    def __init__(self,color,mileage,gears,seats,maxspeed):
        self.color=color
        self.mileage=mileage
        super().__init__(gears,seats,maxspeed)
    def race_mod(self):
        print("Race mode on")
class verna(car,hyundai,hyundai_india): # Three classes inherited (car,hyundai,hyundai_india)
    def __init__(self,gears,seats,maxspeed,city):
        car.__init__(self,gears,seats,maxspeed)
        hyundai.__init__(self)
        hyundai_india.__init__(self,city)
class PAL_V(car):
    def movement(self):
        print("Moving the care forward,backward,upward,downward because this is an flying car!")
v1=volvo("Red and Green","23km/lit.",4,4,220)
print(f"Volvo car color is {v1.color},mileage is {v1.mileage},total gears {v1.gear},seats {v1.seat} and maximum speed is {v1.maxspeed}")
v1.speedup()
v1.apply_break()
v1.movement()
v1.race_mod()
m1=verna(5,6,240,"Gurgaon,Haryana")
print("Maruti car total gear is {},number of seats is {} and maximum speed is {}".format(m1.gear,m1.seat,m1.maxspeed))
m1.speedup()
m1.apply_break()
m1.movement()
print(m1.brandname)
print(m1.city)
p1=PAL_V(6,2,350)
print(f'total gear is {p1.gear},seats is {p1.seat} and maximum speed is {p1.maxspeed}')
p1.speedup()
p1.apply_break()
p1.movement()