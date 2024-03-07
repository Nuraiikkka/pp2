#1
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(x, y):
    return x * y

result = reduce(multiply, numbers)

print("Multiplication of all numbers:", result)

#2
def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

input_string = input("Enter a string: ")

upper, lower = count_upper_lower(input_string)

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

#3
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4
import time
import math

def calculate_square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result

number = int(input(""))
milliseconds = int(input(""))

square_root = calculate_square_root_after_milliseconds(number, milliseconds)

print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")

#5
def all_elements_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(all_elements_true(tuple1))
print(all_elements_true(tuple2))