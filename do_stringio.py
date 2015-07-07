from io import StringIO

f=StringIO()
f.write("hello")
f.write(" ")
f.write("world!")
print(f.getvalue())

f=StringIO("alskdjlksjdfl\n\jsldfj\n a;sdflgj\n l;asdjfg;l ")
while True:
    s=f.readline()
    if s == '':
        break
    print(s.strip())
