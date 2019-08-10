age = 20
name = "Swaroop"

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

print('f-string')
# end='' prevent newline character from being printed (no new line). Can end with a space  ' '
print(f'{name} was {age} years old when he wrote this book.', end=' ')
print(f'Why is {name} playing with that python?')