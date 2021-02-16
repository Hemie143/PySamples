# dict
car1 = {
    'brand': 'bmw',
    'mileage': 99400,
    'color': 'blue'
}
car2 = {
    'brand': 'audi',
    'mileage': 57200,
    'color': 'black'
}
print(car1)                     # {'brand': 'bmw', 'mileage': 99400, 'color': 'blue'}
print(car2['mileage'])          # 57200
car2['mileage'] = 157200
print(car2['mileage'])          # 157200
car2['automatic'] = True
print(car2)                     # {'brand': 'audi', 'mileage': 157200, 'color': 'black', 'automatic': True}

# tuple
