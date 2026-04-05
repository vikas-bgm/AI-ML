#check if file exists or not - isfile() method of os module is used to check if a file exists or not. It returns True if the file exists, otherwise False.

import os

print(os.path.isfile("data.txt"))                # True, because data.txt exists in the current directory
print(os.path.isfile("hello.txt"))               # False, because hello.txt does not exist in the current directory

if os.path.isfile("dat.txt"):                    # this is to avoid FileNotFoundError, if we try to open a file that does not exist
    f = open("data.txt", mode='r')
    # do some operations
    f.close()
else:
    print("File does not exist")