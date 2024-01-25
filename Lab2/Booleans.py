#Example 1/ Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Example 3/ Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

#Example 4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Example 5/ Most Values are True
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Exampple 6/ Some Values are False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Example 7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Example 8/ Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

#Example 9 
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Example 10
x = 200
print(isinstance(x, int))

#Exeercise 1
print(10>9) #True

#Exercise 2
print(10 == 9) #False 

#Exercise 3
print(10 < 9) #False 

#Exercise 4
print(bool("abc")) #True

#Exercise 5
print(bool(0)) #False



