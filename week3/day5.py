#type error = wrong type, value error = wrong value, key error, file not found error
"""data = {"name": "Saima"}
print(data["age"])

int("12")

#try / except (core concept)
try:
    x = int(input("Enter number: "))
except ValueError:
    print("Please enter a valid number")"""

try:
    x = int("abc")
except Exception as e:
    print(e)

#final : runs always despite error
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Done")

"""while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Only numbers allowed")

password = input("Enter password: ")

if len(password) < 6:
    raise ValueError("Password too short")"""