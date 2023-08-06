# Multi level inheritance:- there is a  class, and it inherits multiple class and also inherit itself. mro()- method resolution order use for
class x:
    pass
class y:
    pass
class z:
    pass
class p(x,y):
    pass
class q(y,z):
    pass
class r(p,q,z):
    pass
print(r.mro())