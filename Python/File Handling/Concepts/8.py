# write content from one file to another

with open("data.txt", mode='r') as f:
    data = f.read()
    

with open("data_copy.txt", mode = 'w') as f_copy:
    f_copy.write(data)


# Another way to copy content 

with open ("data1.txt", mode='r') as f1, open("data_copy1.txt", mode='w') as f2 :
    for line in f1:
        f2.write(line) 