import re
x = 'abbaaaababbbab'
matches = re.findall("ab{2,3}", x)
print("Found matches:", matches)
