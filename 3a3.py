#Counting number of zero's in a number
m=int(input())
def count(m):
    if m%10==0 and m!=0:
        return 1+count(m//10)
    elif m==0:
        return 0
    else:
        return count(m//10)
if (m==0):
    print(1)
else:
    print (count(m))
