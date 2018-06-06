#Question 2
"""
for x in range(1000):
    if x%7==0:
        print (x)
"""
#Question 1
"""
n=1
while n<=100:
    if n%2==0:
        print (n)
    n=n+1
"""
#Question 3
"""
n=8
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range (i):
        print("* ",end="")
    print ("")
"""
#Break statement
"""
for i in range(1,30):
    if i%9==0:
        break
    print (i)
"""
#Prime Number between 1-100
"""
from math import sqrt
print("2")

for x in range(3,100,2):
    flag=0
    for i in range (2,int(sqrt(x))+1):
        if x%i==0:
            flag+=1
    if flag==0:
        print (x)
"""
wap which will find all such numbers which are divisible by 7 but not by 5 bt 2000 and 3200 (Inclusive)
print in comma seperated sequence in single line

wap to compute factorial of given numbers 
