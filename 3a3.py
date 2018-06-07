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


#Another method
def count2(n):
    if n<=9:
        if n==0:
            return 1
        else :
            return 0
    if n%10==0:
        return 1+count2(n//10)
    return count2(n//10)
print(count2(m))
