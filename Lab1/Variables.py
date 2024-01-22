#Creating Variable/Example 2
x = 5
y = "John"
print(x)
print(y)

#Example 2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Many Values to Multiple Variables/Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables/Example 
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection/Example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))


#Output Variables/Example 1
x = "Python is awesome"
print(x)

#Example 2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Example 3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Example 4
x = 5
y = 10
print(x + y)

#Example 5
x = 5
y = "John"
print(x, y)

#Global Variables/Example 1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Example 2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword/Example 1
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Example 2
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Exercise 1
carname = "Volvo"

#Exercise 2
x = 50

#Exercise 3
x = 5
y = 10
print(x + y)

#Exercise 4
x = 5
y = 10
z = x + y
print(z)

#Exercise 5
x, y, z = "Orange", "Banana", "Cherry"

#Exercise 6
x = y = z = "Orange"

#Exercise 7
def myfunc():
  global x
  x = "fantastic"
