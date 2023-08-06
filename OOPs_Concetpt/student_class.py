class student:
    def __init__(self,sname,age,standerd,gender):
        self.sname=sname
        self.age=age
        self.standerd=standerd
        self.gender=gender
def main():
    s1=student("Ravi Kumar",12,"6TH","Male")
    s2=student("Rakhi",10,"5TH","Female")
    print(s1.sname,s1.age,s1.standerd,s1.gender)
    print(s2.sname, s2.age, s2.standerd, s2.gender)
if __name__=='__main__':
    main()