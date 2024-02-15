#1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())
        
man = StringManipulator()

man.input_string = input("Enter a string: ")

man.printString()

#2
class shape: 
    def area(self):
        return 0

class square(shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

leng = int(input())
squa = square(leng)
print(squa.area())

#3 
class shape: 
    def area(self):
        return 0

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

leng = int(input())
wid = int(input())
recta = rectangle(leng, wid)
print(recta.area())

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x}, {self.y}")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Moved to: {self.x}, {self.y}")

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x1 = int(input("x point 1: "))
y1 = int(input("y point 1: "))
point1 = Point(x1, y1)

x2 = int(input("x point 2: "))
y2 = int(input("y point 2: "))
point2 = Point(x2, y2)

point1.show()

distance = point1.dist(point2)
print(f"Distance: {distance:.2f}")

#5
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

us_inp = input()

numbers = list(map(int, us_inp.split()))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print( prime_numbers)


