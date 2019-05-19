# number of available cars
cars = 100
# number of passengers in one car with driver
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passangers = 90
# cars withour drivers
cars_not_driven = cars - drivers
# cars with drivers
cars_driven = drivers
# maximum number of passengers which can be transportedn
carpool_capacity = cars_driven * space_in_a_car
# average number of passenger per car
avarage_passangers_per_car = passangers / cars_driven

print('There are', cars, 'cars available')
print('There are only', drivers, 'drivers available')
print('There will be', cars_not_driven, 'emty cars today')
print('We can transport', carpool_capacity, 'people today')
print('We have', passangers, 'to carpool today')
print('We need to put about', avarage_passangers_per_car, 'in each car')
