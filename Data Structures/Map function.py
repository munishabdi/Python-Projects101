
# Map function - is used to produce the result of list iterables
# how do we get the list of prices in this list

items = [
    ("Product", 29),
    ("Product", 9),
    ("Product", 45)
]

prices = []
for item in items:
    prices.append(item[1])

prices.sort()
print(prices)

# the best way to map this list of prices

map_prices = list(map(lambda item:item[1], items))
print(map_prices)
# this will result a map object which is iterable 
# so either use the list() function or iterate over it 

