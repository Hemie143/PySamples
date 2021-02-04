# namedtuple: immutable
from collections import namedtuple

Car = namedtuple('Car', ['brand', 'model'])
my_car = Car('Fiat', 500)
print(my_car.brand)             # Fiat
print(my_car.model)             # 500
print(my_car[0])                # Fiat
print(my_car)                   # Car(brand='Fiat', model=500)

brand, model = my_car
print(brand)                    # Fiat
print(*my_car)                  # Fiat 500

class MyCustomCar(Car):
    def country(self):
        if self.brand == 'Fiat':
            return 'Italy'

f = MyCustomCar('Fiat', 'Uno')
print(f.country())              # Italy

ColorCar = namedtuple('ColorCar', Car._fields + ('color', ))
print(ColorCar('Fiat', 'Punto', 'Red'))         # ColorCar(brand='Fiat', model='Punto', color='Red')

print(f._asdict())              # {'brand': 'Fiat', 'model': 'Uno'}
other_car = f._replace(model='Panda')
print(other_car)                # MyCustomCar(brand='Fiat', model='Panda')
new_car = Car._make(['Fiat', 'Tipo'])
print(new_car)                  # Car(brand='Fiat', model='Tipo')
