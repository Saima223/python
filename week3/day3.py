nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 != 0, nums))

words = ["hi", "hello", "hey", "world"]
h_words = list(filter(lambda w: w.startswith("w"), words))

print(evens)
print(h_words)


students = [
    {"name": "A", "marks": 50},
    {"name": "B", "marks": 80},
    {"name": "C", "marks": 70}
]
#print(students)

xyz = sorted(students, key=lambda x: x["marks"])
print(xyz)
"""
lambda → quick mini function
map() → transform data
filter() → reduce data
sorted() → organize data

PRACTICE 
Double all numbers
Get only numbers > 10
Sort list of names by length
Remove empty strings from list
"""