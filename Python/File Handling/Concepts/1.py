# Syntax for file handling

f = open("data.txt", mode='r')            # mode can be 'r' for read, 'w' for write, 'a' for append, etc.
if f:
    print("File opened successfully")       
else:
    print("Error opening file")

print("Is file readable: ", f.readable())   # File methods , readable() returns True if the file is readable, otherwise False
f.close()                                 # close the file after use

print(f)                                  #<open file 'data.txt', mode 'r'>

print("File name is", f.name)             # File name is data.txt
print("Is file closed ? : ",f.closed)                         # True, because we have closed the file
