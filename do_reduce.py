from functools import reduce

CHAR_TO_INT ={
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9
}

def str2int(s):
    ints=map(lambda ch: CHAR_TO_INT[ch],s)
    return reduce(lambda x,y:x*10+y,ints)

print(str2int("0"))
print(str2int("12300"))
print(str2int("0012345"))


CHAR_TO_FLOAT ={
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    ".":-1
}

def str2float(s):
    nums=map(lambda ch: CHAR_TO_FLOAT[ch],s) 
    point=0
    def to_float(f,n):
        nonlocal point
        if n==-1:
            point=1
            return f
        if point == 0:
            return f*10+n
        else:
            point = point*10
            return f+n/point
    return reduce(to_float,nums,0.0)

print(str2float("0"))
print(str2float("123.456"))
print(str2float("123.45600"))
print(str2float("0.1234"))
print(str2float(".1234"))
print(str2float("120.0034"))
        


def normalize(name):
    return name[0:1].upper() + name[1:].lower()

L1=["adam", "LISA", "barT"]
print(list(map(normalize,L1)))


def prod(L):
    return reduce(lambda x,y: x*y, L)

print("3*5*7*9= ", prod([3,5,7,9]))

def str22float(s):
    def str2list(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,".":"."}[s]
    ss=list(map(str2list,s))
    l=len(ss)-1-ss.index(".")
    ss.remove(".")
    return reduce(lambda x,y: x*10+y,ss)/10.0**l

print(str22float("123.4567"))
