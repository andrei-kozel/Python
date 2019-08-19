from orange import Orange
from person import Person

person = Person('Andrei', 25)
orange = Orange("Citruc", 12, 'orange', 1.2, True, person, 36)

print(orange.buyer.print_name())

print(f'Today {orange.buyer.print_name()} bought {orange.amount} oranges for {round(orange.full_price())}kr')

orange.change_price(40)
print(f"Ooops! New price for 1kg! {orange.price}kr")
