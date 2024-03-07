#1 
a = input()
x = tuple(a.split(','))
res = all(bool(element) for element in x)
print(res)

# 2 '/tmp/example.txt'
import os
path = input()

if os.path.exists(path):
    print(f"The path '{path}' exists.")
else:
    print(f"The path '{path}' does not exist.")
    exit()

if os.access(path, os.R_OK):
    print(f"The path '{path}' is readable.")
else:
    print(f"The path '{path}' is not readable.")

if os.access(path, os.W_OK):
    print(f"The path '{path}' is writable.")
else:
    print(f"The path '{path}' is not writable.")

if os.access(path, os.X_OK):
    print(f"The path '{path}' is executable.")
else:
    print(f"Path '{path}' is not executable.")

#3
import os
path = input()

if os.path.exists(path):
    print(f"The path '{path}' exists.")
    
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print(f"Path '{path}' does not exist.")

# The path '/home/user/documents/example.txt' exists.
# Filename: example.txt
# Directory: /home/user/documents
    
#4
a = input()
try:
    with open(a, 'r') as file:
        line_count = sum(1 for line in file)
    print(f"Number of lines in the file: {line_count}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error: {e}")

#5
a = input("by commas: ")
my_list = a.split(',')
file_path = input("filename:")
try:
    with open(file_path, 'w') as file:
        for item in my_list:
            file.write(item.strip() + '\n')
    print(f"written to {file_path}")
except Exception as e:
    print(f"Error: {e}")

#6
import string
content = input("content to write: ")
for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"
    try:
        with open(file_name, 'w') as file:
            file.write(content + "\n")
        print(f"Created {file_name}")
    except Exception as e:
        print(f"Failed {file_name}: {e}")

#7
a = input("source file: ")
d = input("destination: ")

try:
    with open(a, 'r') as x:
        with open(d, 'w') as f:
            content = x.read()
            f.write(content)
    print(f"copied from {a} to {d}.")
except FileNotFoundError:
    print("does not exist.")
except Exception as e:
    print(f"error: {e}")

#8
import os
a = input("path of the file to delete: ")

if os.path.exists(a):
    if os.access(a, os.W_OK):
        try:
            os.remove(a)
            print(f"'{a}' has been deleted.")
        except Exception as e:
            print(f"Failed to delete: {e}")
    else:
        print("not writable and may not be deleted")
else:
    print("does not exist")




