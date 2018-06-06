#Product of 2 numbers m and n
m=int(input())
n=int(input())
def multiply(x,y):
    if y==1:
        return x
    elif y==0:
        return 0
    else:
        return x+multiply(x,y-1)
print(multiply(m,n))
