
# Functions - A function in programming is a reusable block of code
# that performs a specific task or set of tasks.

def hell_func():
    return "Hello function"


print(hell_func())

# passing parameters


def hell_func(greeting):
    return f"Hello {greeting}"


print(hell_func('Munasar'))

# *args and **kwargs


def student_info(*args, **kwargs):
    print(args)  # returns a tuple of positional arguments
    print(kwargs)  # returns a dictionary with all key-word arguments


# unpacking the values of args and kwargs
courses = ('Math', 'Art')
info = {'name': 'munasar', 'age': 22}

student_info(*courses, **info)
 