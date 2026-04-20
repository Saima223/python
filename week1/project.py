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