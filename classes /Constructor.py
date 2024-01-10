
# Constructor - 
# whats defined inside of the special constructor is called parameters
# self always needs to be defined in convention

class Point:
    def __init__(self, x, y):
        self.x = x # this is instance attributes 
        self.y = y # is used to define class objects 

    def draw(self):
        print(f'point({self.x}, {self.y})')
        print(f"{self.x}, {self.y}")

point = Point(1,2)
point.draw()
# when calling the draw method we didn't have to define the self instance 
# its done automatically

