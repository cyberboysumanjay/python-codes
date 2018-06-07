def linearSearch(a,x):
    for i in range(len(a)):
        if x==a[i]:
            return i
        return -1


a=list(map(int, input().split()))
b=int(input())
print(linearSearch(a,b))
