#ternary
marks = 85
grade = "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 60 else "F"
print(grade)  # B

#value if (condition) else

age = 20
status = "adult" if age >= 18 else "minor"

# With variables
score = 75
grade = "pass" if score >= 50 else "fail"

# Inline in print
name = "Alice"
print("Hello, " + name if name else "Hello, stranger")

count = 0 #0, 1,2,3,4,5
while count < 5:
    print(count)#0, 1,2,3,4
    count += 1 #count = count + 1, count= 1, 2,3,4,5
else:
    print("count is should be less then 5")