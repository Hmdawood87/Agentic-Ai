print("Hello"); 
print("How are you?")

print("I am",25 ,"and the number")
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)
z="dawood"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x = 5
y = 10
print(x + y)
x = 5
y = "John"
print(x , y)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E555
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print("He is called 'Johnny'")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
b = "Hello, World!"
print(b[-5:-2])
a = " Hello,    World!     2"
print(a.strip())
a = "Hello"
b = "World"
c = a + "     " + b
print(c)
age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
txt = f"The price is {price:.12f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)
txt = "We are the so-called \"Vikings\" from the north."
print(txt)