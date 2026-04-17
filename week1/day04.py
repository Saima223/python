# --- Booleans ---
print(5 > 3)          # True
print(5 == 5)         # True
print(5 != 5)         # False
print(type(True))     # <class 'bool'>

# Truthy / falsy 
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool(None))     # False
print(bool(1))        # True
print(bool("hello"))  # True

# --- Logical operators ---
age = 20
has_id = True
print(age >= 18 and has_id)    # True
print(age < 18 or has_id)      # True
print(not has_id)              # False

# --- Grade classifier ---
marks = int(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks!")
elif marks >= 90:
    print("Grade: A+ — Excellent!")
elif marks >= 75:
    print("Grade: A  — Very Good")
elif marks >= 60:
    print("Grade: B  — Good")
elif marks >= 40:
    print("Grade: C  — Pass")
else:
    print("Grade: F  — Fail")

# --- Ternary (one-liner if) ---
result = "Pass" if marks >= 40 else "Fail"
print(f"Result: {result}")
