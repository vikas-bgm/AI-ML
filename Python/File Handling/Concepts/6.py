# Find the numer of lines ,words, characters in a text file.

with open("data1.txt", mode='r') as f:
    no_of_lines = 0
    no_of_words = 0
    no_of_chars = 0
    for line in f:
        no_of_lines += 1                   # to get the number of lines in the file, we simply increment the no_of_lines variable by 1 for each line in the file
        line =line.strip("\n")            # to remove the newline character from the end of the line, so that it does not count as a character
        no_of_chars+=len(line)                         # to get the number of characters in the line, including spaces
        list1 = line.split()
        no_of_words+=len(list1)                         # to get the number of words in the line, we split the line into a list of words using the split() method, and then we get the length of that list
 
print("Number of lines in the file is : ", no_of_lines)
print("Number of words in the file is : ", no_of_words)
print("Number of characters in the file is : ", no_of_chars)       