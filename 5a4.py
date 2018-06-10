n=int(input())
def countZeros(n):
    count=0
    if n>=5:
        return n//5+countZeros(n//5)
    else:
        return count
print(countZeros(n))
