#1 
import math
a = float(input("Input degree: "))
radian = (a * math.pi) / 180
print("Output radian: " + str(radian))

#2
import math
h = int(input("Height: "))
a = int(input("Base1: "))
b = int(input("Base2: "))
area_trap = ((a + b)/2)*h
print("Area of a trapezoid: " + str(area_trap))

#3
import math
h = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
ap = s / (2 * math.tan(math.pi / h))
area_polygon = (h * s * ap) / 2
print("The area of the polygon is: " + str(area_polygon))

#4
import math
a = int(input("Length of base:"))
b = int(input("Height of parallelogram:"))
area = a * b 
print("Area of a parallelogram: " + str(area))

