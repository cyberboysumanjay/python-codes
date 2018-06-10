n=int(input())
print('1')
for i in range(1,n):
    for k in range(i+1):
        if k==i or k==0:
            print(i,end="")
        else:
            print(0,end="")
    print()
