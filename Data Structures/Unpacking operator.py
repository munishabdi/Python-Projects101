
# Unpacking operator

numbers = [1,2,3]
print(*numbers)

# creating list

values = list(range(5))
values = [*range(5), *'Hello']
print(values)

# combining multiple list
first = [1,2]
second = [3]
values = [*first, *second, *"World"]
print(values)