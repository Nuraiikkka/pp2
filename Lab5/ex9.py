import re
a = input()
x = re.sub(r"(?<!^)([A-Z])", r" \1", a)
print(x)