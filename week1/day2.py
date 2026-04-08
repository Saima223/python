# -------------------------------
"""
Data types (int, float, str, bool)
✔ type() function
✔ Type casting (int(), float(), str())
✔ Error concept ('2' + 2)
✔ f-strings ({value:.2f} formatting)
✔ Real practical program (GST calculator)
"""
# DATA TYPES + TYPE CASTING DEMO
# -------------------------------

# Basic variables
a = 10
b = 3.5
c = "Hello"
d = True

print("----- DATA TYPES -----")
print(a, "->", type(a))
print(b, "->", type(b))
print(c, "->", type(c))
print(d, "->", type(d))


# -------------------------------
# TYPE CASTING
# -------------------------------

print("\n----- TYPE CASTING -----")

x = "2"

# Conversions
x_int = int(x)
x_float = float(x)
x_str = str(10)

print(f"Original value: {x} -> {type(x)}")
print(f"String to int: {x_int} -> {type(x_int)}")
print(f"String to float: {x_float} -> {type(x_float)}")
print(f"Int to string: {x_str} -> {type(x_str)}")

# Example of error (commented to avoid crash)
# print("2" + 2)  # ❌ TypeError

# Correct way
print(f"Correct addition after conversion: {int('2') + 2}")


# -------------------------------
# PRACTICAL: GST CALCULATOR
# -------------------------------

print("\n----- GST CALCULATOR -----")

# Taking input
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))

# Calculation
subtotal = price * qty
gst = subtotal * 0.18
final_amount = subtotal + gst

# Output using f-strings
print("\n----- BILL -----")
print(f"Price: {price}")
print(f"Quantity: {qty}")
print(f"Subtotal: {subtotal:.2f}")
print(f"GST (18%): {gst:.2f}")
print(f"Final Amount: {final_amount:.2f}")