#Program to check valid csv file format

import csv

def check_csv(file):
    with open(file,mode='r') as f:
        data = csv.reader(f,delimiter=',')
        header = next(data)                           # to get the header row of the csv file
        no_of_columns = len(header)            # to get the number of columns in the csv file 
        for rec in data:
            if len(rec)!= no_of_columns:                # to check if the number of columns in each row is same as the number of columns in the header row
                print("Invalid csv file format")
                return False
            
        print("Valid csv file format") 
        return True
check_csv("S3batch.csv")
