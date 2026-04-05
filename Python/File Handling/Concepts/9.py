# f.writelines()

with open("data-w.txt", mode='w') as f:
    list_lines= ["Line 1\n", "Line 2\n", "Line 3\n"]      # list of lines to write to the file
    #f.writelines(list_lines)                             # writelines() method is used to write a list of lines to a file. It takes a list of strings as an argument and writes each string to the file without adding any newline characters. Therefore, we need to include the newline characters in the strings themselves, as shown in the example above.
    
    f.write("\n".join(list_lines))                             # Another way to write a list of lines to a file is to use the join() method to concatenate the list of lines into a single string, with newline characters in between each line. This can be more efficient than using writelines(), as it reduces the number of write operations to the file.
    