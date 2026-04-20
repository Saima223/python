# ===============================
# 1. BASIC SYNTAX
# ===============================
#List comprehension = loop + condition + transformation in one line

nums = [1, 2, 3, 4]

# normal loop
result_loop = []
for x in nums:
    result_loop.append(x * 2)

# list comprehension
result_comp = [x * 2 for x in nums]

print("Loop:", result_loop)
print("Comprehension:", result_comp)


# ===============================
# 2. WITH CONDITION
# ===============================

nums = [-2, -1, 0, 1, 2, 3]

positive = [x for x in nums if x > 0]

print("\nPositive numbers:", positive)


# ===============================
# 3. EXPRESSION + CONDITION
# ===============================

nums = [1, 2, 3, 4, 5]

even_squares = [x**2 for x in nums if x % 2 == 0]

print("\nEven squares:", even_squares)


# ===============================
# 4. IF-ELSE INSIDE
# ===============================

nums = [1, 2, 3, 4]

labels = ["even" if x % 2 == 0 else "odd" for x in nums]

print("\nEven/Odd labels:", labels)


# ===============================
# 5. NESTED COMPREHENSION
# ===============================

matrix = [[1, 2], [3, 4], [5, 6]]

flat = [item for row in matrix for item in row]

print("\nFlattened list:", flat)


# ===============================
# 6. RANGE EXAMPLE
# ===============================

squares = [x**2 for x in range(6)]

print("\nSquares:", squares)


# ===============================
# 7. REAL-WORLD EXAMPLES
# ===============================

# 💰 Prices discount
prices = [100, 200, 300]
discounted = [p * 0.9 for p in prices]

print("\nDiscounted prices:", discounted)


# 📞 Filter valid phone numbers
numbers = ["9876543210", "123", "9999999999"]
valid = [n for n in numbers if len(n) == 10]

print("Valid numbers:", valid)


# 👤 Clean names
names = ["  aman", "rahul  ", " sara "]
clean = [n.strip().title() for n in names]

print("Clean names:", clean)


# ===============================
# 8. MINI PRACTICE
# ===============================
#Filter only even numbers
#uppercase list
#get only prices > 100 and apply 10% discount
#make a list of squares

nums = [1, 2, 3, 4, 5]

# squares
squares = [x**2 for x in nums]
print("\nSquares:", squares)

# even numbers
evens = [x for x in nums if x % 2 == 0]
print("Evens:", evens)

# uppercase
fruits = ["apple", "banana"]
upper = [f.upper() for f in fruits]
print("Uppercase:", upper)

# flatten
nested = [[1, 2], [3, 4]]
flat = [x for row in nested for x in row]
print("Flatten:", flat)

# real task
prices = [100, 250, 80, 400]
filtered_discount = [p * 0.9 for p in prices if p > 100]

print("Filtered + discounted:", filtered_discount)