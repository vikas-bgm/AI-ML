#Parsing Json data

import json

data = {'name': "vikas", 'age': 28, 'role': "devops",'city':"Bangalore"}

json_data = json.dumps(data)            # dumps() method converts a Python object into a JSON string
print(json_data)                      # {"name": "vikas", "age": 28, "role": "devops", "city": "Bangalore"}

data1 = ["abc", 20, False, None]
print(json.dumps(data1))                