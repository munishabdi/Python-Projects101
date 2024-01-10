
# Unpacking list

numbers = [1,2,3]
first, second, third = numbers
print(numbers)
# leftside elements has to match the rightside elements 

# packing the items on the list
numbers = [1,2,3,3,3,3,3,3,4,4,99]
first, last, *other = numbers
print(first, other)
