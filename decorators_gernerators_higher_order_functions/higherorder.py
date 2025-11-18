nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  
from functools import reduce

nums = [1, 2, 3, 4]
sum_total = reduce(lambda a, b: a + b, nums)
print(sum_total)  
