"""
def changeString(a,c1,c2):
    b=list(a)
    for i in range(len(b)):
        if b[i]==c1:
            b[i]=c2
    return b
print (changeString("Happy",'p','a'))
"""
def changeString(a,c1,c2):
    b=list(a)
    if b[len(b)-1]==c1:
        b[len(b)-1]=c2
        return b
    else:
        b=b[0:-1]
        return changeString("".join(b),c1,c2)
print (changeString("Happy",'p','a'))
