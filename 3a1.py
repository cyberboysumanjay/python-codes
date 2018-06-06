#Sum of all numbers less than n
n=int(input())
sum=0
def s(x):
    if x==1:
        return 1
    elif x==0:
        return 0
    else:
        return x+s(x-1)
print(s(n))
