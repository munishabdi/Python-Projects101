
# Exceptions
# Handling exceptions
# the (else) block will be executed if no exceptions is thrown
try: 
    age = int(input("age: "))
except ValueError:
    print("You didnt enter a valid age.")
else:
    print("No exceptions were thrown.")