age = int(input("Enter your age: "))
marks = float(input("Enter your percentage: "))
experience = int(input("Enter years of experience: "))
license = input("Do you have a driving licence? (yes/no): ").lower()

has_lic = True if license == "yes" else False

failed_reasons = []

# Rule 1: Age check
if age < 18 or age > 35:
    print("Age not eligible")
    failed_reasons.append("Age criteria failed")

# Rule 2: Marks check
if marks < 60:
    print("Academic cutoff not met")
    failed_reasons.append("Marks criteria failed")

# Rule 3: Experience OR License
if experience < 2 and not has_lic:
    print("Need 2yr experience or driving licence")
    failed_reasons.append("Experience/License criteria failed")


# Final result
if len(failed_reasons) == 0:
    print("Congratulations! You are eligible 🎉")
else:
    print("\nYou are NOT eligible ❌")
    print("Reasons:")
    for reason in failed_reasons:
        print("-", reason)