
# creating a basic calculator


'''
if conditions that will allow us to create logic of the 
calculations. we will use exceptions to catch any human errors

'''
while True:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    operation = input("Select the operation: (+, -, *, /) ")
    try:

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: can't divide zero number")
                result = None

        if result is not None:
            print('result: ', result)

    except ValueError:
        print("Please enter a valid number")
    except Exception as e:
        print(e)
        result = None

    play_again = input("Play again: (yes/no) ")
    if play_again != 'yes':
        break
print("Bye!")
