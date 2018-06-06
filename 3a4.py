#Geometric Progression using recursion
m=int(input())
def GP(k):
    if k==0:
        return 0
    else:
        return 1/2**(k-1)+GP(k-1)
print(GP(m))
