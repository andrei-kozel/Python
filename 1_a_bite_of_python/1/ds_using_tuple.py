zoo = ('python', 'elephant', 'penguin')
print(f'Number of animals in the zoo is {len(zoo)}')

new_zoo = ('monkey', 'camel', zoo)
print(f'Number of animals in the new zoo is {len(new_zoo)}')
print(f'All animal in new zoo are {new_zoo}')
print(f'Last animal brought from old zoo is {new_zoo[2][2]}')

