
# Inheritance - class can inheirt attributes and methods from another class
# each of the child(sub) classes inherit all the methods and attributes from animal class
# Methods are basically functions associated with classes
# Attributes are variables used to define class values

class Animal:
    alive = True
        
    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")
    
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

# these child classes could've their own methods 
# objects(instance of class) 

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# child mothods - 
print(rabbit.alive)
fish.swim()
rabbit.run()
hawk.fly()