thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Set Items - Data Types: String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

#type() - <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor - set() constructor to make a set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#To add one item to a set use the add() method: 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method. Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
   print(x)

#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#True and 1 is considered the same value:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)

#Exercise 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Exercise 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Exercise 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Exercise 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
  
#Exercise 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

