# ===============================
# 1. CREATING LISTS
# ===============================

prices = [100, 200, 300]
names = ["Rahul", "Aman", "Sara"]
mixed = [1, "hello", 3.5, True]

print("Prices:", prices)
print("Names:", names)
print("Mixed:", mixed)


# ===============================
# 2. INDEXING (0-based)
# ===============================

print("\nIndexing:")
print(prices[0])   # first
print(prices[1])   # second
print(prices[-1])  # last (negative indexing)


# ===============================
# 3. SLICING
# ===============================

nums = [10, 20, 30, 40, 50]

print("\nSlicing:")
print(nums[1:4])   # [20,30,40]
print(nums[:3])    # first 3
print(nums[::2])   # step
print(nums[::-1])  # reverse


# ===============================
# 4. ADDING ELEMENTS
# ===============================

nums = [1, 2, 3]

nums.append(4)             # add one
nums.extend([5, 6])        # add multiple
nums.insert(1, 100)        # insert at index

print("\nAfter adding:", nums)


# ===============================
# 5. REMOVING ELEMENTS
# ===============================

nums.remove(100)   # remove by value
nums.pop()         # remove last
nums.pop(1)        # remove by index

print("\nAfter removing:", nums)


# ===============================
# 6. SORT & REVERSE
# ===============================

nums = [3, 1, 4, 2]

nums.sort()
print("\nSorted:", nums)

nums.reverse()
print("Reversed:", nums)


# ===============================
# 7. LENGTH
# ===============================

print("\nLength:", len(nums))


# ===============================
# 8. REAL DATA EXAMPLE (PRICES)
# ===============================

prices = [120, 340, 560, 220]

print("\nTotal:", sum(prices))
print("Max:", max(prices))
print("Min:", min(prices))

prices.sort()
print("Sorted prices:", prices)


# ===============================
# 9. REAL DATA EXAMPLE (CUSTOMERS)
# ===============================

customers = ["Aman", "Rahul", "Sara"]

customers.append("John")
customers.sort()

print("\nCustomers:", customers)


# ===============================
# 10. MINI PRACTICE
# ===============================

my_list = [10, 20, 30, 40, 50]

# first & last
print("\nFirst:", my_list[0])
print("Last:", my_list[-1])

# reverse
print("Reversed:", my_list[::-1])

# add values
my_list.append(60)
my_list.extend([70, 80])

# remove values
my_list.remove(20)
my_list.pop()

print("Final list:", my_list)