
# Method Chaining - is basically overriding or replacing a method in the base class
# if you still want to initialize the age constructor, use super class

class Animal:

    def __init__(self):
        # print('Animal Constructor')
        self.age = 1

    def eat(self):
        print("This animal is eating")

# Animal: parent, Base
# Mammal: child sub


class Mammal(Animal):
    def __init__(self):
        print('Mammal Constructor')
        self.weight = 2
        super().__init__()  # calling the animal constructor

    def walk(self):
        print("This animal is walking")


class Fish(Mammal):
    def swim(self):
        print("This Fish is swiming")


mammal = Mammal()
print(mammal.weight)
print(mammal.age)
