"""
def changeString(a,c1,c2):
    b=list(a)
    for i in range(len(b)):
        if b[i]==c1:
            b[i]=c2
    return b
a="Test"
"""
def changeString(a,c1,c2):
    b=list(a)
    if(len(b)>0):
        if b[0] == c1 :
            print (c2)
            b=b[1:len(b)]
            changeString(".join(b)",c1,c2)
        else:
            print (b[0])
            b=b[1:len(b)]
            changeString(".join(b)",c1,c2)
    else:
        return


print (changeString("Happy",'p','a'))
