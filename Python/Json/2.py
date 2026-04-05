#json.dump() method is used to write a Python object into a file in JSON format.

import json

config_data = {
    "env": "prod",
    "servers": ["app1", "app2", "app3"],
    "timeout": 60
}

with open("config.json", mode='w') as f:
    json.dump(config_data,f,indent= 4)
    print("File written successfully")