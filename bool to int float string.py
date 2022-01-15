Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=20
y=30
z=bool(x>y)
print(z)
False
x=2.5
y=3.6
z=bool(x=y)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    z=bool(x=y)
TypeError: bool() takes no keyword arguments
z=bool(x<y)
print(z)
True
x=str(2)
y=bool(x)
print(y)
True
x=str(2)
y=str(5)
z=bool(y>x)
print(z)
True
