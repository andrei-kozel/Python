class Apple:
    def __init__(self, color, size, weight, fresh):
        self.color = color
        self.size = size
        self.weight = weight
        self.fresh = fresh


apple = Apple('red', 3, 12, True)
print(apple)
print(apple.size)
