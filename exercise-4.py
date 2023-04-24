import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

parse = json.dumps(sampleJson, sort_keys=True, indent = 2)

print(parse)