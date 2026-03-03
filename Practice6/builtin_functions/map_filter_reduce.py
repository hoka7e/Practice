from functools import reduce
nums = [1, 2, 3, 4, 5, 6]

doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)

evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)

product = reduce(lambda x, y: x * y, nums)
print("Product:", product)