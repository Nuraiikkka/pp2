#Strings/Example 
print("Hello")
print('Hello')

#Assign String to a Variable/Example
a = "Hello"
print(a)

#Multiline Strings/Example - double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Example - single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#Slicing/Example - from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])

#Slice From the Start/Example - from the start to position 5 (not included)
b = "Hello, World!"
print(b[:5])

#Slice To the End/Example -  from position 2, and all the way to the end
b = "Hello, World!"
print(b[2:])

#Negative Indexing/Example - From: "o" in "World!" (position -5); To, but not included: "d" in "World!" (position -2)
b = "Hello, World!"
print(b[-5:-2])


#Modify Strings
#Upper Case/Example 
a = "Hello, World!"
print(a.upper())

#Lower Case/Example 
a = "Hello, World!"
print(a.lower())

#Remove Whitespace/Example 
a = " Hello, World! "
print(a.strip()) #returns "Hello, World!"

#Replace String/Example
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String/Example 
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation/Example - Merge variable a with variable b into variable c
a = "Hello"
b = "World"
c = a + b
print(c)

#Example - To add a space between them, add a " "
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format/Example 1
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Example 2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Example 3
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Escape Character 
txt = "We are the so-called \"Vikings\" from the north."
#print(txt)

#Exercise 1
x = "Hello World"
print(len(x))

#Exercise 2
txt = "Hello World"
x = txt[0]

#Exercise 3
txt = "Hello World"
x = txt[2:5]

#Exercise 4
txt = " Hello World "
x = txt.strip()

#Exercise 5
txt = "Hello World"
txt = txt.upper()

#Exercise 6
txt = "Hello World"
txt = txt.lower()

#Exercise 7
txt = "Hello World"
txt = txt.replace("H", "J")

#Exercise 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))