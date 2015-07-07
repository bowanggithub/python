from io import BytesIO

f=BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

data="遥遥切克闹，煎饼果子来一套".encode("utf-8")
f=BytesIO(data)
print(f.read())
