#Exercise 1.1 [without input]
def grto(grams):
    conv = 28.3495231
    ounces = grams * conv
    return ounces
print(grto(100))

#Exercise 1.2 [with input]
def grto(grams):
    conv = 28.3495231
    ounces = grams * conv 
    return ounces
grams = input()
grams = int(grams)
ounces = grto(grams)
print(ounces)

#Exercise 1.3 [without Function]
grams = input()
grams = int(grams)
conv = 28.3495231
ounces = grams * conv
print(ounces)

#Exercise 2
def fartocel(fahrenheit): 
    return 5/9  * (fahrenheit - 32)
far = float(input())
cel = fartocel(far)

print(f"{cel}")

#Exercise 3
def solve(numheads, numlegs):
    rab = (numlegs - 2 * numheads) // 2
    chick = numheads - rab
    if rab >= 0 and chick >= 0 and 4 * rab + 2 * chick == numlegs:
        return rab, chick
    else: 
        return None, None
numheads = 35
numlegs = 94
rab, chick = solve(numheads, numlegs)
print(f"rabbits:{rab}, chicken: {chick}")

#Exercise 4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

numbers = [int(x) for x in input().split()]
prime_numbers = filter_prime(numbers)
print(f"Prime numbers: {prime_numbers}")

#Exercise 5
def print_perm(x, answer=''):
    if len(x) == 0:
        print(answer)
        
    for i in range(len(x)):
        char = x[i]
        left = x[0:i]
        right = x[i + 1:]
        a = left + right
        print_perm(a, char + answer)
        
n = input()
print_perm(n)

#Exercise 6
def reverse_sent(sen):
    words = sen.split()
    rev_words = words[::-1]
    rev_sent = ' '.join(rev_words)
    return rev_sent
a = input()
reversed_v = reverse_sent(a)
print(reversed_v)

#Exercise 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#Exercise 8
def spy_game(nums):
    code = [0, 0, 7, 'x']
    
    for num in nums: 
        if num == code[0]:
            code.pop(0)
            
        if len(code) == 1: 
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#Exercise 9
import math
def vol_cal(r):
    volume = (4/3) * math.pi * (r**3)
    return volume
radius = int(input())
volume_cal = vol_cal(radius)
print(volume_cal)

#Exercise 10
def u_elem(a):
    unique_list = []
    for element in a:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
orig_str = input()
orig_list = orig_str.split()
orig_list = [int(i) for i in orig_list]

llist = u_elem(orig_list)
print(llist)

#Exercise 11
def is_palin(s: str) -> bool:
    n = ''.join(c for c in s.lower() if c.isalpha())
    return n == n[::-1]
check_palin = input()
fff = is_palin(check_palin)
print(fff)

#Exercise 12
def histogram(num):
    for a in num:
        histo = '*' * a
        print(histo)

lls = input()
lls = lls.split()
lls = [int(i) for i in lls]

histogram(lls)

#Exercise 13
import random

def guess_the_number_game():
    print("Hello! What is your name?")
    name = input()

    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number_game()





