''' JSON Config Validator
Problem:

You are given a JSON config file like:
{
  "env": "prod",
  "servers": ["app1", "app2"],
  "timeout": 30
}
Requirements:
Check if required keys exist:
env
servers
timeout
servers must be a list
timeout must be integer
Raise proper errors
💡 Real-world use:
Terraform config validation
App config validation before deployment
'''