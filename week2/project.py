"""
Complete program using lists, dicts, loops, comprehensions, and conditions. Closest to real analyst work so far.
01. Collect N students (name + marks) via input(), store as list of dicts
02. Compute stats: average, highest, lowest — using list comprehensions
03. Sort by marks, assign grades, print formatted table with ranks
04. Show pass/fail counts and pass percentage
05. Bonus: group by grade and show count per grade
06. Bonus: search for a student by name and show their rank
"""
# 1. Collect N students
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students.append({"name": name, "marks": marks})

# 2. Compute stats using list comprehension
marks_list = [s["marks"] for s in students]

avg_marks = sum(marks_list) / len(marks_list)
highest = max(marks_list)
lowest = min(marks_list)

print("\n--- STATS ---")
print("Average:", round(avg_marks, 2))
print("Highest:", highest)
print("Lowest:", lowest)

# 3. Sort by marks & assign grades
students_sorted = sorted(students, key=lambda x: x["marks"], reverse=True)

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Assign grade and rank
for i, s in enumerate(students_sorted):
    s["grade"] = get_grade(s["marks"])
    s["rank"] = i + 1

# Print formatted table
print("\n--- STUDENT TABLE ---")
print(f"{'Rank':<5} {'Name':<10} {'Marks':<10} {'Grade':<5}")
for s in students_sorted:
    print(f"{s['rank']:<5} {s['name']:<10} {s['marks']:<10} {s['grade']:<5}")

# 4. Pass/Fail stats
passed = len([s for s in students if s["marks"] >= 40])
failed = len(students) - passed
pass_percentage = (passed / len(students)) * 100

print("\n--- PASS/FAIL ---")
print("Passed:", passed)
print("Failed:", failed)
print("Pass %:", round(pass_percentage, 2))

# 5. BONUS: Group by grade
grade_count = {}
for s in students_sorted:
    grade = s["grade"]
    grade_count[grade] = grade_count.get(grade, 0) + 1

print("\n--- GRADE COUNT ---")
for g, count in grade_count.items():
    print(g, ":", count)

# 6. BONUS: Search student by name
search_name = input("\nEnter name to search: ")

found = False
for s in students_sorted:
    if s["name"].lower() == search_name.lower():
        print("\nStudent Found:")
        print(f"Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}, Rank: {s['rank']}")
        found = True
        break

if not found:
    print("Student not found")