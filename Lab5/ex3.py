import re
text = "it is_me"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print(matches)
