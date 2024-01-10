
# Instance varaibles - are the varibles declared inside the constructor
# Class variables - used to set some default values/variables

class Car:

    wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.make} is driving")

    def stop(self):
        print(f"This {self.make} is stopped")


# objects(instance)
car1 = Car('Chevy', 'Coverette', 2023, 'red')
car2 = Car('Toyota', 'Tocoma', 2013, 'orange')

print(car1.wheels)
print(car1.make)
print(car2.make)

car1.drive()
car2.stop()