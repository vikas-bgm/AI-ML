#

import csv

with open("sample.csv", mode='r', encoding='utf-8') as f:
    data = csv.DictReader(f, delimiter='|')
    for row in data:
        print(row)