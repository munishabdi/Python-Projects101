
# Class vs Instance of attributes
# instance attributes - are the (x,y) parameters defined in the object class
# class attributes/vairables - are defined on the top of the constructor
    # they're same across all instances of the class

class Point:
    default_color = 'red'
    def __init__(self, x, y):
        self.x = x # this is instance attributes 
        self.y = y # is used to define class objects 

    def draw(self):
        print(f'point({self.x}, {self.y})')
        print(f"{self.x}, {self.y}")

Point.default_color = 'Yellow'
# using the class reference 

point = Point(1,2)
print(point.default_color)
print(Point.default_color)