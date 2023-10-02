print("Hello, World!") #This is a comment

# Python variables
x = 5
y = "testing"
print(x)
print(y)

a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

a = "Python "
b = "love "
c = "me "
print(a + b + c)

x = "love"

def myfunc():
  global x
  x = "love"

myfunc()

print("Python is " + x)

# Python data types

x = str("Hello World")                        # str
x = int(20)                                   # int
x = float(20.5)                               # float
x = complex(1j)                               # complex
x = list(("apple", "banana", "cherry"))       # list
x = tuple(("apple", "banana", "cherry"))      # tuple
x = range(6)                                  # range
x = dict(name="John", age=36)                 # dict
x = set(("apple", "banana", "cherry"))        # set
x = frozenset(("apple", "banana", "cherry"))  # frozenset
x = bool(5)                                   # bool
x = bytes(5)                                  # bytes
x = bytearray(5)                              # bytearray
x = memoryview(bytes(5))                      # memoryview

# Python Number

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))