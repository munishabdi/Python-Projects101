
# Inheritance

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
fish = Fish()

print(mammal.age)
fish.eat()
print(fish.swim())