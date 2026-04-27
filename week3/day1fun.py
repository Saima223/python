#function syntx 
#default parameters
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("tony") #argument

#using return 
def stats(numbers):
    return sum(numbers), max(numbers), min(numbers)

s, mx, mn = stats([10, 20, 30])

#multiple return values python return a tuple
def stats(numbers):
    return sum(numbers), max(numbers), min(numbers)

s, mx, mn = stats([10, 20, 30])

#local vs global: local does not effect global
x = 10   # global

def test():
    x = 5   # local
    print(x)

test()       # 5
print(x)     # 10

#calling function inside function
def square(x):
    return x * x

def print_square(num):
    result = square(num)
    print(result)