
# a class is a blueprint for creating objects. Objects are instances of a class, 

x = 1
print(type(x))

class Point:
    def draw(self):
        print("draw")


# objects
point = Point()
point.draw()
print(isinstance(point, Point))