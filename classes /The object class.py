
# The object Class

class Animal:
    
    def __init__(self):
        self.age = 1

    def eat(self):
        print("This animal is eating")

# Animal: parent, Base
# Mammal: child sub 
class Mammal(Animal):
    def walk(self):
        print("This animal is walking")

class Fish(Mammal):
    def swim(self):
        print("This Fish is swiming")

mammal = Mammal()
print(isinstance(mammal, Animal))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object)) # indirectly inherits from Object class

# mammal is an instance of Mammal class
# mammal is also an intance of Animal class since it inherits 
# Animal also inherits from object, True


