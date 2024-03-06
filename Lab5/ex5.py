import re
a = input()
pattern = r"a.*b$"
match = re.search(pattern, a)
if match:
    print("Yes")
else:
    print("No")


