
# Conditionals

# language = 'Java'

# if language == 'Python':
#     print("the langudage is python")
# elif language == 'Java':
#     print("the language is java")
# else:
#     print("No match")
# print("please guess the correct language! ")

# Boolean logical operators
# and - both condition has to be true
# or  - only one of the conditions must be true
# not - it reverses the condition to false if it were true, and vice versa

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print("Verified Access is Granted")
else:
    print("Please check if your creds")

# Identity objects (is):
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b)  # checks for equality - true
print(a is b)  # checks for identity object in memory - false

# you can assing a = b, which is true
a = b
print(id(a) == id(b))
# This is true because a is assigned to b

# False values
# False
# None
# Zero of any numberic type
# any empty sequence. for ex: '', [], ()
# any empty mapping. for ex: {}

condition = 'Test'
if condition:
    print("Executed to True")
else:
    print("Executed to False")
