def changeString(a,c1,c2):
    b=[]
    for i in range(len(a)):
        if a[i]==c1:
            b.append(c2)
        else:
            b.append(a[i])
    c="".join(b)
    return c
a=input("Enter String\n")
c1=input("Enter the character you want to replace\n")
c2=input("Enter the character you want to add\n")
print(changeString(a,c1,c2))
