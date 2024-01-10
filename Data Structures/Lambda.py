
# Lmabda - anonymous function which can be used only one time

items = [
    ("Product", 29),
    ("Product", 9),
    ("Product", 45)
]

# def sort_items(item):
#     return item[1]

# items.sort(key=sort_items)
# print(items)

# instead, we can use lambda
# lambda syntax, [lambda parameter:expression]
items.sort(key=lambda item:item[1])
print(items)