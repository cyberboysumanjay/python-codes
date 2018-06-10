s='XDAcADXa'
n=len(s)
for i in range(3,n-1):
    b=[]
    if ord(s[i])>=97 and ord(s[i])<=122:
        if ord(s[i-1])>=65 and ord (s[i-2])>=65 and ord(s[i-3])>=65 and ord(s[i+1])>=65 and ord (s[i+2])>=65 and ord(s[i+3])>=65:
            if ord(s[i-1])<=90 and ord(s[i-2])<=90 and ord(s[i-3])<=90 and ord(s[i+3])<=90 and ord(s[i+1])<=90 and ord(s[i+2])<=90:
                    b.append(s[i])
print (b)
