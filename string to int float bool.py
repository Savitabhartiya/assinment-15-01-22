Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=str(50)
y=str(2.5)
z=str(40)
print(int(x))
50
print(int(y))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(int(y))
ValueError: invalid literal for int() with base 10: '2.5'
print(float(y))
2.5
print(bool(x>z))
True
