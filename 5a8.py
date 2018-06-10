n=int(input())
l=[]
for i in range(n+1):
    if i%2==1:
        l.append(i)
for i in range(n,0,-1):
    if i%2==0:
        l.append(i)
print(l)
