# Instance and class variables
# Class variable are like global variable so it accessible
class mobile:
    wireless=True
    year=2020
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
    M1=mobile("Apple","Black",True)
    print(M1.brandname)
    print(M1.color)
    print(M1.IsJack)
    M1.calling()
    M1.cameraclick()
    M1.message()#No need
    M1.screen="LED" # Specific attribute for M1 only it is not common for everyone
    print(M1.screen)
    print(M1.year,M1.wireless)
    mobile.message(M1)# Then ask for an object
    print("..............................................................!")
    M2=mobile("Google","While-Green",False)
    print(M2.brandname)
    print(M2.color)
    print(M2.IsJack)
    M2.calling()
    M2.message()
    M2.cameraclick()
    print(M2.year,M2.wireless)
    #print(M2.screen)# screen-No attribute of M2
if __name__=='__main__':
    main()
