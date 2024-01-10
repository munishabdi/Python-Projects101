
# Guessing numbers

from random import randint

lower_number, higher_number = (1, 10)
random_number = randint(lower_number, higher_number)
print(
    f"guess the number from range of {lower_number} to {higher_number} ")

max_attempt = 3
attempt = 0

while True:
    try:
        user_guess = int(input("Guess: "))
    except ValueError:
        print("Please enter a valid number")
        continue
        # continue statement skips the current iteration and start a new iteration

    if user_guess > random_number:
        print("The number is lower")
    elif user_guess < random_number:
        print("The number is higher")
    else:
        print("You guessed the number! ")
        break
    attempt += 1

    if attempt == max_attempt:
        print(
            f"You have exceeded the max attempt, the correct number is {random_number}")
