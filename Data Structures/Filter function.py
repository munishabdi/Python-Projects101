
# Filter Function
# filter this list and get the items with price greater or equal to 10 
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 45)
]

# Option1
prices = []
for item in items:
    if item[1] >= 10:
        prices.append(item[1])

print(prices)

# Option2
filter_price = list(filter(lambda item:item[1] >= 10, items))
print(filter_price)