from math import sqrt
def quadraticRoots(a,b,c):
    d=b*b-4*a*c


    if d>0:
        r1=(-b+sqrt(d))/2*a
        r2=(-b-sqrt(d))/2*a
        print("Nature of Roots: ")
        print(1)
        print ("Roots are ",r1,r2)
    elif d==0:
        r1=(-b+sqrt(d))/2*a
        print("Nature of Roots: ")
        print(0)
        print ("Root is",r1)
    else:
        print("Nature of Roots: ")
        print(-1)

quadraticRoots(1,2,2)
