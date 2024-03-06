import re
x = 'abbaaaaba'
match = re.findall("ab*", x)
print(match)
