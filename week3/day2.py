#lambda arguments: expression
square = lambda x: x * x
print(square(4))
xyz = square(5)
print(xyz)


nums = [1, 2, 3, 4]

result = map(lambda x: x*x, nums)
print(list(result))   # [1, 4, 9, 16]

#Keep only matching items
nums1 = [1, 2, 3, 4, 5, 6]
result1 = filter(lambda x: x % 2 == 0, nums1)
print(list(result1))   # [2, 4, 6]

raw_salaries = ["₹45,000", "₹1,20,000", "₹30,000", "₹75,500", "₹50,000"]

result = sorted(
    filter(
        lambda x: x > 50000,
        map(lambda x: int(x.replace("₹", "").replace(",", "")), raw_salaries)
    ),
    reverse=True
)

print(result)