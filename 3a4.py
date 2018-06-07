#Geometric Progression using recursion
m=int(input())
def GP(k):
    if k==0:
        return 1
    else:
        return 1/2**(k)+GP(k-1)
print(GP(m))
