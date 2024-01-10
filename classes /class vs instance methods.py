
# Class vs Intance methods

class Point:
    default_color = 'red'
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    # classmethod
    @classmethod
    def zero(cls):
        cls(0,0)

    def draw(self):
        print(f'point({self.x}, {self.y})')
        print(f"{self.x}, {self.y}")

point = Point(1,2)
