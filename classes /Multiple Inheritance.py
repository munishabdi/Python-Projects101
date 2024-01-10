
# Multiple inheritance -

class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person):
    def greet(self):
        print("Employee Greet")

person = Person()
manager = Manager()
manager.greet()
# prints employee greet because we added the employee class first 
