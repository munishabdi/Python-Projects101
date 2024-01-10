
# sorting list - list and string are easy, but tuple sort is complex
# the sort method takes two parameters
# key and reverse - to change the sort order

numbers = [3, 44, 2, 20, 7]
numbers.sort()
print(numbers)
# numbers are sorted in ascending order

# for descending order
numbers.sort(reverse=True)
print(numbers)

# Sorted function - function takes an iterable
# iterable
# key & everse
print(sorted(numbers, reverse=True))
print(numbers)
# returns in descending order



items = [
    ("Product", 29),
    ("Product", 9),
    ("Product", 45)
]

items.sort()
print(items)
# python doesn't know how to sort this list
# we need to define a function that python will use to sort the list

def sort_items(item):
    return item[1]

items.sort(key=sort_items)
print(items)