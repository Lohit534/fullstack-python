import json
result = {}

inp =  '{"name": "Alice", "age": 30}'
result = json.loads(inp) 
result = json.dumps(result) 
print(type(result))
