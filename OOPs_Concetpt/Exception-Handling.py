'''Exception handling:-
Errors- 1) Syntax error- it is compiled time error(code not complied) like: some typing mistakes. Easy to find it
2) Logical error: not easy to find because the program is compiled and run, but it will show incorrect output
because the logic is incorrect.
3) Runtime error: That stage the program will stop
for handling these errors and print somthing, it should not appropriately stop the program it is good practice in coding
'''
a=int(input())
b=int(input())
#print(a//b) # it work fine but if we input b=0  then it give runtime error for handling this
try:
    print(a//b)
except Exception:
    print("integer division or modulo by zero")
print("<-----------------------------****--------------------------->")
c=input()
try:
    print(a+c)
except Exception as e: # Exception handle every error,while also use for specific error:TypeError,ValueError..
    print(e)
print("<------------------------------***---------------------------->")
#a=int(input()) # If enter any string then it'll give the error not handel by exception handler because this is out side the Try block
try:
    a=int(input()) # So need to inside the try block
    print(a)
except Exception as e:
    print(e)
print("<---------------------------------***------------------------->")
arr=[1,2,3,4,5,6]
try:
    print(arr[10])
except Exception as e:
    print(e)
# If we want to print somthing anyway while an error or not an error but print/execut it for that we use finally
finally:
    print("Finally this is important to print")