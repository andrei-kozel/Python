class Fruit():
    def __init__(self, fruit_type, amount, color, weidth, freshness, buyer, price_for_kilo):
        self.fruit_type = fruit_type
        self.amount = amount
        self.color = color
        self.weidth = weidth
        self.freshness = freshness
        self.buyer = buyer
        self.price = price_for_kilo

    def full_price(self):
        return self.weidth * self.price

    def change_price(self, new_price):
        self.price = new_price
