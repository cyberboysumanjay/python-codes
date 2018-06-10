#n=input()
def printSubstrings(n):
    l=[]
    for i in range(len(n)):
        for j in range(i+1,len(n)+1):
            print(n[i:j])
print(printSubstrings("xyz"))
