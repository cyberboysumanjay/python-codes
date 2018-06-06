#Sum of digits using recursion
def digitSum(x):
    if x<10:
        return x
    else:
        return x%10+digitSum(x//10)
m=int(input())
print(digitSum(m))
