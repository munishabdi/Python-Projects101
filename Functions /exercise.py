
# FizzBuzz Algorithm 
# if number is divisible by 3 and remainder is 0 print fizz
# # if number is divisible by 5 and remainder is 0 print Buzz
# if number is divisible by 3 and 5 and remainder is 0 print fizzBuzz

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number

print(fizzbuzz(19))