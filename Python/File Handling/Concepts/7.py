#writing to a file

with open("data_w.txt", mode='w') as f:
    data = f.write("Hello there, welcome to file handling in Python")      # write() method is used to write data to a file. It takes a string as an argument and writes it to the file. If the file already exists, it will be overwritten.
    print(data)                                          # 57, because the length of the string is 57 characters
    