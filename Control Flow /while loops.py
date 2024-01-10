
# While loops: we use it to repeat something as long as a condition is true

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ''
# while command != 'quit':
#     command = input('> ').lower()
#     print("ECHO", command)

""" How the above code works:
    we set command to empty string
    while command is not equal to 'quit'
    keep getting input from the user
"""

name = ''
while len(name) == 0:
    name = input("Enter your name? ")

print(f"Hello {name}")