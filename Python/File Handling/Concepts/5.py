#Reading data from a file

with open("data.txt", mode='r') as f:
    data1 = f.read(3)
    data = f.read()                             #read() is a method that reads the entire contents of the file and returns it as a string. If the file is large, it may consume a lot of memory. In such cases, it's better to read the file in chunks or line by line using methods like readline() or readlines().
    print(data) 
    print(data1)
    
with open("data1.txt",mode='r') as fr:
    dat = fr.readline()
    dat1 = fr.readline()
    print(dat)                            # readline() is a method that reads a single line from the file and returns it as a string. It reads characters from the file until it encounters a newline character ('\n') or reaches the end of the file (EOF). Each time you call readline(), it will return the next line in the file, allowing you to process the file line by line.
    print(dat1)
    
with open("data1.txt",mode='r') as g:
    data = g.readlines()
    print(data)                            # readlines() is a method that reads all the lines from the file and returns them as a list of strings. Each element in the list corresponds to a line in the file, including the newline character ('\n') at the end of each line. This method is useful when you want to process the file line by line or when you need to access specific lines in the file.
    
with open("data1.txt", mode='r') as h:
    for line in h:                         # we can also read a file line by line using a for loop. This is an efficient way to read large files, as it does not load the entire file into memory at once.
        print(line,end="")                  # end="" is used to avoid adding an extra newline character after each line, as each line already ends with a newline character. 
        #print(h.tell())                             # tell() is a method that returns the current position of the file pointer in bytes. It indicates how many bytes have been read from the file so far. This can be useful for tracking the progress of reading a file or for debugging purposes.
       # h.seek(0)                               # seek() is a method that allows you to change the current position of the file pointer. In this case, we are using seek(0) to move the file pointer back to the beginning of the file, so that we can read it again from the start.
        #print("After seek -")
