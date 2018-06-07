"""
A child is running up a staircase of n steps. He can move 1,2 or 3 steps at a time.
Count Number of possible ways can he run up the stairs. Return all possible number of ways

def countSteps(k):
    if k<=2:
        return k
    elif k==3:
        return 4
    else:
        return countSteps(k-1)+countSteps(k-2)+countSteps(k-3)
m=int(input())
print(countSteps(m))
"""

def sumA(a,n):
    aa,bb=0,0
    for i in range(0,n,2):
        aa+=a[i]
    for i in range (1,n,2):
        bb+=a[i]
    return abs(aa-bb)

a = list(map(int, input().rstrip().split()))
n=len(a)
print(sumA(a,n))
