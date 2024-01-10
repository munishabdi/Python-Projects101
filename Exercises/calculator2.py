
# creat a basic calculator
try:
    number1 = int(input('Enter a number: '))
    number2 = int(input('Enter a number: '))
    operation = input("Select math operation: (+, -, *, / ): ")

    if operation == "+":
        result = number1 + number2

    elif operation == "-":
        result = number1 - number2

    elif operation == "*":
        result = number1 * number2

    elif operation == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            print("error: cant divide zero number")

except ValueError:
    print("Please enter a valid input")
except Exception as e:
    print(e)
    result =  None
else:
    if result is not None: # anthing other than None, and saying if result != None
        print("result:", result)
# the if result is not None -  represents whether the result has value other than None
# if it does a have other None, then it makes the condition True and print result is 
        # executed, but if result is None and the condition becomes false, nothing is done
