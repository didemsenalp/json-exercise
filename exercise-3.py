import json

sampleJson = {"key1": "value1", "key2": "value2"}

parsed = json.dumps(sampleJson,indent=2, separators=(',', ': '))

print(parsed)