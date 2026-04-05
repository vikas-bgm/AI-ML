# Covert json to python dict    

import json

config_data = {
    "env": "prod",
    "servers": ["app1", "app2", "app3"],
    "timeout": 60,
    "application": "fe",
    "db": "rds"
}

# converts to json string
data = json.dumps(config_data)
print(data)
print(type(data))

# Convert json to python dict

data1 = json.loads(data)
print(data1)
print(type(data1))