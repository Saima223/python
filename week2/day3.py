# ===============================
# 1. FOR LOOP WITH range()
# ===============================
#Print numbers 1 to 20 using range()
#[10, 25, 60, 80, 45] → print only values > 50
#Count how many numbers are even


print("For loop with range:")
for i in range(5):   # 0 to 4
    print(i)

print("\nCustom range:")
for i in range(1, 10, 2):  # start, end, step
    print(i)


# ===============================
# 2. LOOPING OVER A LIST
# ===============================

names = ["Aman", "Rahul", "Sara"]

print("\nLoop over list:")
for name in names:
    print(name)


# ===============================
# 3. WHILE LOOP
# ===============================

print("\nWhile loop:")
i = 0
while i < 5:
    print(i)
    i += 1   # IMPORTANT (otherwise infinite loop)


# ===============================
# 4. BREAK
# ===============================

print("\nBreak example:")
for i in range(10):
    if i == 5:
        break   # stop loop completely
    print(i)


# ===============================
# 5. CONTINUE
# ===============================

print("\nContinue example:")
for i in range(5):
    if i == 2:
        continue   # skip this iteration
    print(i)


# ===============================
# 6. ENUMERATE (index + value)
# ===============================

names = ["Aman", "Rahul", "Sara"]

print("\nEnumerate:")
for index, name in enumerate(names):
    print(index, name)


# ===============================
# 7. REAL USE — STUDENT MARKS
# ===============================

marks = [45, 67, 82, 30, 90]

print("\nAll marks:")
for m in marks:
    print(m)


# Pass/Fail
print("\nPass/Fail:")
for m in marks:
    if m >= 50:
        print(m, "Pass")
    else:
        print(m, "Fail")


# Find topper
topper = marks[0]
for m in marks:
    if m > topper:
        topper = m

print("\nTopper marks:", topper)


# Count students who passed
count = 0
for m in marks:
    if m >= 50:
        count += 1

print("Students passed:", count)


# ===============================
# 8. USING ENUMERATE (BETTER)
# ===============================

print("\nMarks with index:")
for i, m in enumerate(marks):
    print("Student", i, "marks:", m)


# ===============================
# 9. BREAK + CONTINUE IN REAL CASE
# ===============================

print("\nStop if fail found:")
for m in marks:
    if m < 35:
        print("Fail found:", m)
        break


print("\nSkip failed students:")
for m in marks:
    if m < 50:
        continue
    print("Passed:", m)