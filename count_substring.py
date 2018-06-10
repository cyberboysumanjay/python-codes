s='bbababababbbab'
def countSubstring(s,ss):
    a=len(ss)
    count=0
    for i in range(len(s)):
        if s[i:i+a]==ss:
            count=count+1
    return count
print(countSubstring(s,'ab'))
