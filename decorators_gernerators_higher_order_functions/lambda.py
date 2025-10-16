
# Lambda Function Examples in Python

# 1. Add Two Numbers
add = lambda a, b: a + b
print("Add 5 + 3:", add(5, 3))

# 2. Find Maximum of Two Numbers
maximum = lambda x, y: x if x > y else y
print("Maximum of 10 and 25:", maximum(10, 25))

# 3. Square of a Number
square = lambda x: x * x
print("Square of 4:", square(4))

# 4. Even or Odd
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print("11 is:", even_odd(11))

# 5. Reverse a String
reverse = lambda s: s[::-1]
print("Reverse of 'Python':", reverse("Python"))

# 6. Using with map()
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print("Squares of [1,2,3,4]:", squares)

# 7. Using with filter()
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers in [1-6]:", evens)

