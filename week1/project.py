"""
 marks loop program
Write a program that collects student names and marks from user input (stop when they type "done"), then prints total students, average, highest, lowest, and lists who passed and who failed.
01. Use a while True loop with break to collect input
02. Store names and marks as separate lists (or one list of pairs)
03. Use a for loop with enumerate to process results
04. Format all output cleanly with f-strings
05. Bonus: add input validation so marks must be 0–100
"""
age = int(input("Enter your age: "))
marks = float(input("Enter your percentage: "))
experience = int(input("Enter years of experience: "))
license = input("Do you have a driving licence? (yes/no): ").lower()

has_lic = True if license == "yes" else False

is_eligible = True   

# Rule 1: Age check
if age < 18 or age > 35:
    print("Age not eligible")
    is_eligible = False

# Rule 2: Marks check
if marks < 60:
    print("Academic cutoff not met")
    is_eligible = False

# Rule 3: Experience OR License
if experience < 2 and not has_lic:
    print("Need 2yr experience or driving licence")
    is_eligible = False


# Final result
if is_eligible:
    print("Congratulations! You are eligible ")
else:
    print("\nYou are NOT eligible ")