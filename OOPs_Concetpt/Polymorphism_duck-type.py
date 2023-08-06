''' Polymorphism: Poly + Morphism => Poly- Many & Morphism- form/behaviour
Many forms/many behaviours of a single thing(Many uses of a single thing),like it means operator overloading.
method overloading not supported in python, it can be done using if-else condition, but it can way-around(Jugaad) not properly define.
Duck type: is a special case of dynamic type (if the behaviour of a bird exactly same like duck then we'll call
that bird is a duck, I do not care the bird are duck or not if the bird same like duck walking,swimming,quack,flying..).
all depends on behaviour.
'''
class jioCaller:
    def call(self):
        print("Calling")
class truCaller:
    def call(self):
        print("Ringing")
        print("Caller data")
class phone:
    def callFunc(self,phoneApp):
        phoneApp.call()
phoneApp=truCaller() # phoneApp was an object and this object can access the call method over the truCaller class
p1=phone()
p1.callFunc(phoneApp)
phoneApp=jioCaller() #its also work because both the classes have the behaviour of call, so don't care weather the class are truCcaller or jioCaller its behaviour is call so it will work
p1.callFunc(phoneApp)
