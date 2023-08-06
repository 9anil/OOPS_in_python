# Operator overloading:
class student:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other): # here is self is s1 and other is s2
        ans1=self.x+other.x
        ans2=self.y+other.y
        #return ans1,ans2,ans1+ans2
        return '{}+{}={}'.format(ans1,ans2,ans1+ans2)
    # less than is __lt__ function
    def __lt__(self,other):
        ans1=self.x+other.x
        ans2=self.y+other.y
        if ans1>ans2:
            return True
        else:
            return False
s1=student(10,20)
s2=student(5,7)
print(s1.x,s1.y,s1.x+s1.y)
s3=s1+s2 # + Type can not add class types, so need to override our inbuilt our add function
print(s3)
if s1>s2:
    print("S1 is grater")
else:
    print("S2 is grater")
