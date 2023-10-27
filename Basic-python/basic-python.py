print("Hello, World!") #This is a comment

# --------------------------------- #
#                                   #
#         Python variables          #
#                                   #
# --------------------------------- #

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

# --------------------------------- #
#                                   #
#         Python datatypes          #
#                                   #
# --------------------------------- #

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

# --------------------------------- #
#                                   #
#         Python numbers            #
#                                   #
# --------------------------------- #

x = 1    # int
y = 2.8  # float
z = 1j   # complex
j = 1 
k = (j + z)

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
print(k)

print(type(a))
print(type(b))
print(type(c))
print(type(k))

# --------------------------------- #
#                                   #
#         Python casting            #
#                                   #
# --------------------------------- #


z = 4.2 

print(type(z))
print(str(z))

# python strings 

a = "Hello, World!"
print(len(a))

a = "Hello, World!"
print(a[7])

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if 'best' in txt:
   print(txt[4:-25])
   print(txt.split('best'))
   print(txt.replace("best","and"))

a = "the"
b = "best"
c = a[2] + a[:2] + b[2]
print(c)
print(len(c))
z = float(len(c))
print(z)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))




