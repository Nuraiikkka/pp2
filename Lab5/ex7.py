import re
a = input()
words = a.split('_')
ccS = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
print(ccS)