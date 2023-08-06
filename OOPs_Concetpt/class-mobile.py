'''Introduction OOPs:
Class is nothing but a templates it is a structure, and we are creating object using this class.
Object is nothing, but it is an instance of the class.
Imperative: a sequence/series of instruction.
OOPs- using imperative paradime
'''
class mobile:
    def __init__(self):
        self.brandname="Sumsung"
        self.color="Red"
        self.IsJack=False
    def calling(self):
        print("Mobile use for calling")
    def message(self):
        print("Message also by mobile")
    def cameraclick(self):
        print("Use for clicking picture")
def main():
    M1=mobile()
    print(M1.brandname)
    print(M1.color)
    print(M1.IsJack)
    M1.calling()
    M1.message()
    M1.cameraclick()
    print("<------------------------------------------------>")
    M2=mobile()
    print(M2.brandname)
    print(M2.color)
    print(M2.IsJack)
    M2.calling()
    M2.cameraclick()
    M2.message()
if __name__=='__main__':
    main()
print("<-------------------* We self pass the data(brandname,color,Jack) in new_mobile class *--------------->")
class new_mobile:
    def __init__(self,brandname,color,IsJack):
        self.brandname=brandname
        self.color=color
        self.IsJack=IsJack
    def calling(self):
        print("Calling")
    def cameraclick(self):
        print("CameraClick")
    def message(self):
        print("Messaging")
def main():
    M1=new_mobile("Apple","Black",True)
    print(M1.brandname)
    print(M1.color)
    print(M1.IsJack)
    M1.calling()
    M1.cameraclick()
    M1.message()
    print("..............................................................!")
    M2=new_mobile("Google","While-Green",False)
    print(M2.brandname)
    print(M2.color)
    print(M2.IsJack)
    M2.calling()
    M2.message()
    M2.cameraclick()
if __name__=='__main__':
    main()
