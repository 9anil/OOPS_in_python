'''Access modifier:- The programmer to protect some variables which are important which can not given to the user to
modify these are three types.
1) Public access modifier:- By default what we use the normal code that we write in oops every variable every
method that can be access anywhere that are public.Access everywhere. variable amount.
2) Protected access modifier:- Only the child class can access the data and methods that present in base class.They can
access the class itself(Base class) and in derived class(child class) also.Protected variable single underscore(_) like: _amount
3) Private access modifiers:- This is most secure no one can access, they can only we access inside the class itself.
only inside the class they are declared. Private Variable is double underscore  (__) like: __amount '''
# Example:- Protected access modifier
print("<---------------------------- Protected access modifier ----------------------------->")
class bank_account:
    _amount=0 # Protected
    def deposite(self,add):
        self._amount+=add
    def debit(self,sub):
        self._amount-=sub
class user1(bank_account):
    def calculateTax(self):
        tax=self._amount*0.2
        print("Tax=",tax)
u1=user1()
u1.deposite(500)
print(u1._amount)
u1.calculateTax()
u1.debit(200)
print(u1._amount)
u1.deposite(1000)
print(u1._amount)
u1.debit(700)
print(u1._amount)
# Example: Private access modifier
print('<----------------------------- Private access modifier ------------------------------>' )
class new_account:
    __new_amount=0 # Private
    def credit(self,add):
        self.__new_amount+=add
    def debit(self,sub):
        self.__new_amount-=sub
    def check_amount(self):
        print(self.__new_amount)
class user(new_account):
    #def Tax(self):
        #Tax=self.__amount*0.2 # Can accessible because it is private, it can only be access inside the class itself
    pass
U1=user()
U1.credit(1000)
#print(U1.__amount) # Can accessible because it is private, it can only be access inside the class itself
a1=new_account()
a1.credit(500)
#print(a1.__amount) # Can accessible because it is private, it can only be access inside the class itself
a1.check_amount()
a1.debit(100)
a1.check_amount()

