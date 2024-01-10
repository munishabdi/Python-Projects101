
# Different Exceptions
# in programming we cant divide a number by 0
# both valueerror and zerodivision can be used in the same except block
try:
    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didnt enter a valid age.")
except ZeroDivisionError:
    print("You didnt enter a valid age.")
else:
    print("No exceptions were thrown.")
