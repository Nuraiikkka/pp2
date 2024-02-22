#1 sqauare generator
def square_generator(num):
    for i in range(1, num + 1):
        yield i**2
a = int(input())
squar_res = square_generator(a)

for square in squar_res:
    print(square)

#2
def even_num_generator(num):
    for i in range(0, num + 1):
        if i % 2 == 0:
            yield i
a = int(input())
ev_num = even_num_generator(a)
print(','.join(map(str, ev_num)))

#3
def three_four_div_generator(num):
    for i in range(0, num + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
a = int(input())
calc = three_four_div_generator(a)
print(','.join(map(str, calc)))

#4 
def squares_generator(a, b):
    for i in range(a, b):
            yield i**2
a = int(input())
b = int(input())
squar_res = squares_generator(a, b)
print(','.join(map(str, squar_res)))

#5
def down_num_generator(n):
    while n >= 0:
        yield n
        n -= 1
a = int(input())
dwon_res = down_num_generator(a)
print(','.join(map(str, dwon_res)))
