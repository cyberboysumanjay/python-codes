s=input()
c='x'
def replaceX(s,c):
    if len(s)>0:
        if s[0]!=c:
            print (s[0],end="")
        s=s[1:]
        return(replaceX(s,c))
replaceX(s,c)
