
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print('successful')
        break

""" this is how the above code works...
    we set successful message to True 
    we iterated the range between 0 - 2
    the first iteration attempted is printed 
    the if condition is checking if the message is True
    if its the successful message is printed 
    and the break statement terminate the loop 
"""

# lets display different message...
# set successful to False and print different message when attempt is failed

count = 0
successful = False
for number in range(3):
    print("Attempt")
    count += number
    if successful:
        print('successful')
        break
print(f"Attempted {count} times but failed")