class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return (self.b * self.h) / 2


tr = Triangle(5, 5)
print(tr.area())
