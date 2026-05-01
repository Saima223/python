import json

# write file
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello 😊")

# read file
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())

# JSON write
data = {"name": "Saima", "age": 60}

with open("data.json", "w") as f:
    json.dump(data, f)

# JSON read
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)

    """
dump() → save to file
load() → read from file
dumps() → just convert to string
    """