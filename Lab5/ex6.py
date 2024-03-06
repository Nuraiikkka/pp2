# import re
# def rep(text):
#     pattern = r'[ ,.]'
#     x = re.sub(pattern, ':', text)
    
#     return x
# exstr = "This is a test, to replace. spaces, commas, and dots."
# repstr = rep(exstr)

# print("Original:", exstr)
# print("Replaced:", repstr)

import re
a = input()
x = re.sub(r"[ ,.]", ':', a)
print(x)