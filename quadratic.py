import math
def quadratic(a,b,c):
    if (a == 0):
        print("not quadratic")
    delta = b*b-4*a*c
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    return x1,x2
