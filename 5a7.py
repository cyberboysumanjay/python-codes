from math import log2
n=int(input())
#print(bin(n))
def decimalToBinary(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return 10**int(log2(n))+decimalToBinary(n-2**int(log2(n)))
print (decimalToBinary(n))
