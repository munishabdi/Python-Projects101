
# Scope - which refers to the region of the code where a variable is defined
# in function variable only use local variable and avoid global ones


message = 'a'

def gree(name):
    global message
    message = 'b'

print(gree('mosh'))
print(message)