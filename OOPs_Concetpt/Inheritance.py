'''Inheritance:-some properties/attribute of child class(derived class) are same to parent class(base class)
(it has parent child relation)'''
# class animal:
#     def __init__(self,type):
#         self.type=type
#     def sleep(self):
class car: # Base class-parent
    def __init__(self,gears,seats,maxspeed):
        self.gear=gears
        self.seat=seats
        self.maxspeed=maxspeed
    def speedup(self):
        print("Speed increasing")
    def apply_break(self):
        print("Speed Decrease")

class Harrier(car):  # Derived class-child
    pass
h1=Harrier(5,4,220)
print(h1.gear)
print(h1.seat)
print(h1.maxspeed)
h1.speedup()
h1.apply_break()
print("<---------------------------------------------------------------------------------------------------->")
class new_car:
    def __init__(self,gears,seats,maxspeed):
        self.gear=gears
        self.seat=seats
        self.maxspeed=maxspeed
    def speedup(self):
        print("New car-Speed increasing")
    def apply_break(self):
        print("New car-speed decreasing")
class volvo(new_car):
    def race_mode(self):
        print("Race mode is on")
class verna(new_car):
    pass
v1=volvo(5,4,240)
V2=volvo(4,6,220)
c1=new_car(5,6,240)
print(f'Total gear {v1.gear} and seats is {v1.seat}, its maximum speed is {v1.maxspeed}.')
v1.speedup()
v1.apply_break()
v1.race_mode()
print("Total gear %d and total seats is %d and maximum speed is %d."%(V2.gear,V2.seat,V2.maxspeed))
V2.race_mode()
V2.speedup()
V2.apply_break()
print("Total gear {} and seats {} and maximum speed is {}".format(c1.gear,c1.seat,c1.maxspeed))
c1.speedup()
c1.apply_break()
# c1.race_mode() - Show error because no attributes of car class
w1=verna(3,10,180)
print(f'Total gear is {w1.gear} and seats is {w1.seat} and maximum speed is {w1.maxspeed}')
w1.speedup()
w1.apply_break()
# w1.race_mode()  - Show error because no attributes of verna class

