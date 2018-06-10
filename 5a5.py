n=int(input())
c=int(input())
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
def product(n):
    if n==0:
        return 0;
    elif n==1:
        return 1
    else:
        return n*product(n-1)

if c==1:
    print(sum(n))
elif c==2:
    print(product(n))
else:
    print(-1)
