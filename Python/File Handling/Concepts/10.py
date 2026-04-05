# Reading csv file 

import csv

with open("S3batch.csv", mode = 'r') as f:
    data = csv.reader(f,delimiter=',')             # csv.reader() method is used to read the csv file, it returns a reader object which is an iterator that can be used to iterate over the lines in the csv file
    #print(data)                                     # <_csv.reader object at 0x7f8c8c8c8c8c>
    next(data)                                      # to skip the header row
    for rec in data:
        print(rec)
print("-------------------------------------------")
#Another was to read is with DictReader

with open("S3batch.csv", mode='r') as d:
    data1 = csv.DictReader(d,delimiter=',')
    for rec1 in data1:
        print(rec1)                                 # OrderedDict([('Name', 'John'), ('Age', '25'), ('City', 'New York')])