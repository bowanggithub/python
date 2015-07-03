s=(x*x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n,a,b=0,0,1
    while n< max:
        yield b
        a,b=b,a+b
        n=n+1
    return "done"


f=fib(10)
print("fib(10):",f)
for x in f:
    print(x)


g=fib(5)
while 1:
    try:
        x=next(g)
        print("g:",x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break



def triangles():
    y=[1]
    yield y
    while 1:
        y=[y[i]+y[i+1] for i in range(0,len(y)-1)]
        y.append(1)
        y.insert(0,1)
        yield y

n=0
for t in triangles():
    print(t)
    n=n+1
    if n==10:
        break
