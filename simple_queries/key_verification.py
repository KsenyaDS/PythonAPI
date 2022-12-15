# name = 'Ксения'
# print(f"Hello from {name}")
import json
string_json = '{"answer": "Hello"}'
obj = json.loads(string_json)
key = "answer"
if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")