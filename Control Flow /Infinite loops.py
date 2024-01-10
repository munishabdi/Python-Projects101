
# Infinite loop - is a loop that runs forever

while True:
    command = input('> ')
    print("ECHO", command)
    if command.lower() == 'quit':
        break
# with this representation, we no longer need to initialze command
# make sure to jump out of this infinite loop using the break 