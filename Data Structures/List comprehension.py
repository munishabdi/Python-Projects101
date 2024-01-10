
# List comprehension
# Syntax = [expression for item in items]
# the prefered way to map and filter list, is list comprehension

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 45)
] 

# equivalent of map function
prices = [item[1] for item in items]
print(prices)

# Filter equivalent 
filter_prices = [item for item in items if item[1] >= 10]
print(filter_prices)
