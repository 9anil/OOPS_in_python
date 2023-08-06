'''
Function: Block of code performing a specific task
Builtin- input(),print(),len(),count(),range()...
User define: user define a function and
'''
# def sum():
#     a,b=23,12
#     print(a+b)
# sum()
# sum()

def add(a,b):
    print(a+b)
def main():
    add(a=int(input()),b=int(input()))
if __name__=='__main__':
    main()
def swap(a,b):
    temp=a
    a=b
    b=temp
    print(a,b)
def main():
    a,b=map(int,input().split())
    swap(a,b)
if __name__=='__main__':
    main()
def addition():
    a,b=map(int,input().split())
    return a+b
def str_var():
    return "Hello World !"
def main():
    x=addition()
    y=addition()
    print(x,y)
    msg=str_var()
    print(msg)
if __name__=='__main__':
    main()