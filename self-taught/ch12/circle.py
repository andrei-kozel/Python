import math


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2


circle = Circle(10)
print(circle.area())
