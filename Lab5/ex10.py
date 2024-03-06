import re
a = input()
ssS = re.sub(r'(?<=[a-z])([A-Z])', r'_\1', a).lower()
print(ssS)