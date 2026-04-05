# Open file with text and binary mode 

with open("data1.txt",mode='r') as f:       #  here encoding happens as mode is text, so we get the data in string format
    data = f.read()
    print(data)

with open("data1.txt",mode='rb') as fb:     # here encoding does not happen as mode is binary, so we get the data in bytes format
    data = fb.read()
    print(data)