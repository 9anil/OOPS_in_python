# Overriding parent class and supper class
# Overriding-When the overriding the method the name of should be the same
class new_car:
    def __init__(self,gears,seats,maxspeed):
        self.gear=gears
        self.seat=seats
        self.maxspeed=maxspeed
    def speedup(self):
        print("New car-Speed increasing")
    def apply_break(self):
        print("New car-speed decreasing")
    def movement(self):
        print("Car moves forward and backword")
class volvo(new_car):
    def __init__(self,color,mileage,gears,seats,maxspeed): # Overriding previous __init__ method so using super keyword
        self.color=color
        self.mileage=mileage
        super().__init__(gears,seats,maxspeed)
    def race_mode(self):
        print("Race mode is on")
class verna(new_car):
    pass
class PAL_V(new_car):
    def movement(self): # Overriding the movement method
        print("Car move forward backward and flying up and down also")
v1 = volvo("Red","20 km/lit",5, 4, 240)
c1 = new_car(5, 6, 240)
print(f'Total gear {v1.gear} and seats is {v1.seat}, its maximum speed is {v1.maxspeed}.')
v1.speedup()
v1.apply_break()
v1.race_mode()
print("Color is {} and Mileage is {}".format(v1.color,v1.mileage))
print("Total gear {} and seats {} and maximum speed is {}".format(c1.gear, c1.seat, c1.maxspeed))
c1.speedup()
c1.apply_break()
p1=PAL_V(6,2,320)
p1.movement()
