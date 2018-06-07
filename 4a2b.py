def checkPalindrome(s):
    if len(s)<2:
        return True
    elif s[0]==s[len(s)-1]:
        return checkPalindrome(s[1:len(s)-1])
    else:
        return False

s=input()
print(checkPalindrome(s))
