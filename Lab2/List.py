mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#access items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#returns the items from the beginning to, but NOT including, "kiwi"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#returns the items from "cherry" to the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Append Items - add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove the first occurance of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Clear the List - empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#example 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#The Syntax: newlist = [expression for item in iterable if condition == True]

#Condition: newlist = [x for x in fruits if x != "apple"]

#With no if statement: newlist = [x for x in fruits]

#Iterable - You can use the range() function to create an iterable: newlist = [x for x in range(10)]

#newlist = [x for x in range(10) if x < 5]

#newlist = [x.upper() for x in fruits]

#newlist = ['hello' for x in fruits]

#Return "orange" instead of "banana": newlist = [x if x != "banana" else "orange" for x in fruits]

#Sort the list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort the list descending alph
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list descending num
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Sort the list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Append list2 into list1: 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#Use the extend() method to add list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Exercise 1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Exercise 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Exercise 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Exercise 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#Exercise 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Exercise 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Exercise 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Exercise 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


