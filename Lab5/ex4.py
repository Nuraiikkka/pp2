import re
text = "it Is me"
matches = re.findall(r'[A-Z]+[a-z]+', text)
print(matches)