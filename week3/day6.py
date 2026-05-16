import json

data = {"name": "tom"}

# convert to string
json_string = json.dumps(data)

print(json_string)        # '{"name": "tom"}'
print(type(json_string))  # str

lines = ["A\n", "B\n", "C\n"]

with open("file.txt", "w") as f:
    f.writelines(lines)