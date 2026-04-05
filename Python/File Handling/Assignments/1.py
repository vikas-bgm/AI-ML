'''You receive a CSV from an external team. You must validate:

Requirements:
File should not be empty
All rows must have same number of columns
No empty values allowed
Print meaningful errors (not just True/False)
'''

import csv

file_name = "S3batch.csv"
errors =[]

try:
    with open(file_name, mode='r') as f:
        data= csv.reader(f,delimiter=',')
        try:
            header =next(data)
        except StopIteration:
            print("File is Empty")
            exit()
        if not header:
            print("File has Empty Header")
            exit()
        no_of_columns = len(header)
        for i, row in enumerate(data, start=2):             # start=2 because header is row 1
            #Cloumn count check
            if len(row) != no_of_columns:
                errors.append(f"Row {i} has inconsistent cloumn count. Expected {no_of_columns} but got {len(row)}")
            #Empty value check
            if "" in row:
                errors.append(f"Row {i} has missing values")
    
    if errors:
        print("Errors found in CSV file:")
        for err in errors:
            print(err)
        else:
            print("CSV file is valid")
except FileNotFoundError:
    print(f"File {file_name} not found")
            