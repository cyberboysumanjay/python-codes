"""
def hello():
    print("Hello")
    print ("Fun")
print ("Zip")
hello()
"""
"""
def printf(a):
    print (a)
printf("Testing")
"""
#Fibonacci using recursion
"""
def fibr(n):
    a,b=0,1
    if n==1:
        return a
    elif n==2:
        return b
    else:
        return fibr(n-1)+fibr(n-2)
"""
#Check Fibonacci
"""
def fib(n):
    a,b=0,1
    if n==1:
        return (a)
    elif n==2:
        return (b)
    else:
        for i in range(n-1):
            a,b=b,a+b
        return (a)

def checkFib(n):
    flag=False
    if n<6 and n!=4:
        flag=True
    for i in range(1,n+1):
        if n==fib(i):
            flag=True
            break
    print(flag)
n=int(input())
checkFib(n)
"""
#Another way to check Fibonacci
"""
x=int(input())
def CheckFib(n):
    flag=False
    a,b=0,1
    if n==0 or n==1:
        flag=True
    else:
        for i in range(n-1):
            a,b=b,a+b
            if n==a or n==b:
                flag=True
                break
            elif a>n or b>n:
                break
    print(flag)
CheckFib(x)



"""
#Prime between 2 to N
"""
from math import sqrt
n=int(input())
print("2")

for x in range(3,n,2):
    flag=0
    for i in range (2,int(sqrt(x))+1):
        if x%i==0:
            flag+=1
    if flag==0:
        print (x)
"""
#Factorial Using recursion
"""
def fact(x):
    if x<2:
        return 1
    else:
        f=x*fact(x-1)
        return f
n=int(input())
print(fact(n))
"""
#Calculating power using recursion
"""
x=int(input())
a=int(input())

def power(x,a):
    if a==2:
        return x*x
    elif a==1:
        return x
    elif a==0:
        return 1
    elif a<0:
        return -1
    else:
        return x*power(x,a-1)
print(power(x,a))

#Printing digits of a numbers
from math import log10
b=int(input())
while b>10:
    c=int(log10(b))
    print(b//power(10,c))
    b%=power(10,c)
print (b)
"""
#Printing digits of number second method
x=int(input())
def printReverse(x):
    if x<10:
        print (x)
    else:
        printReverse(x//10)
        print(x%10)

printReverse(x)
