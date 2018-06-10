"""
class Puppy(object):
    color="Brown"
    name="Shadow"
    def bark(self):
        print("Hello")
        print("I saw ",self.name)
        print("He is ",self.color,"in color")
puppy1=Puppy()
puppy1.bark()
print(puppy1.color)
#puppy2=Puppy("Max","White")
#puppy2.bark()
"""
from math import sqrt
class checkNumber(object):
    def __init__(self,n):
        self.n=n
    def checkPrime(self,n):
        if n==2:
            print ("Prime number")
        flag=0
        for i in range (2,int(sqrt(n))+1):
            if n%i==0:
                flag+=1
        if flag==0:
            print ("Prime number")
        else:
            print ("Not a Prime number")

    def CheckFib(self,n):
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
        if flag==True:
            print("Part of Fibonacci Series")
        else:
            print("Not a part of Fibonacci Series")

n=int(input())
a=checkNumber(n)
a.CheckFib(n)
a.checkPrime(n)
