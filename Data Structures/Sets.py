
# Sets: a collaction with no duplicates

numbers = (1,2,3,3,2,4,4)
uniques = set(numbers)
second = {1,4,6}
second.add(5)
second.remove(1)
print(second)

# mathematical operations
first = set(numbers)

# union of all sets 
newset = first | second
print(newset)

# intersection of two sets
print(first & second)

# difference between two sets
print(first - second)