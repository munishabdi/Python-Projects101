
# *args - takes a variable number of arguments 

def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total

print(multiply(2,3,4,5))