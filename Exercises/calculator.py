
try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    math_operation = input("Select operation: (+, -, *, / ) ")

    if math_operation == "+":
        result = n1 + n2

    elif math_operation == "-":
        result = n1 - n2

    elif math_operation == "*":
        result = n1 * n2

    elif math_operation == "/":
        if n2 != 0:
            result = n1 / n2
        else:
            print("Error: division by zero is not valid")
            result = None
    else:
        print("Please enter a valid operation to continue (+, -, *, /)")
        result = None
        
    if result is not None:
        print("result:", result)


except ValueError:
    print("Please enter a valid operation symbol")
except ZeroDivisionError:
    print("division by zero is not valid")


# GUESSING GAME


from random import randint

lower_num, higher_num = 1, 10
random_number = randint(lower_num, higher_num)

print(f"Guess the number in the range from {lower_num} to {higher_num}")

max_attempts = 3
attempts = 0 

while attempts < max_attempts:
    try:
        user_guess = int(input("Guess: "))
    except ValueError as e:
        print("Please enter a valid number")
        continue

    if user_guess > random_number:
        print("The number is lower")
    elif user_guess < random_number:
        print("The number is higher")
    else:
        print("You guessed it!")
        break

    attempts += 1

if attempts == max_attempts:
    print(f"Sorry, you've reached the maximum number of attempts. The correct number was {random_number}.")
