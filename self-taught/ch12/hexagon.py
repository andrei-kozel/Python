class Hexagon:
    def __init__(self, side):
        self.side = side

    def calculate_perimetr(self):
        return 6 * self.side


hx = Hexagon(6)
print(hx.calculate_perimetr())
