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
car1 = ('bmw', 99400, "blue")
car2 = ('audi', 57200, 'black')
print(car1)                     # ('bmw', 99400, 'blue')
print(car2)                     # ('audi', 57200, 'black')
print(car2[1])                  # 57200
# car2[1] = 157200                # TypeError: 'tuple' object does not support item assignment

# Custom class
class Car:
    def __init__(self, brand, mileage, color):
        self.brand = brand
        self.mileage = mileage
        self.color = color

car1 = Car('bmw', 99400, "blue")
car2 = Car('audi', 57300, 'black')
print(car2.mileage)             # 57300
car2.mileage = 157300
print(car2.mileage)             # 157300
car2.automatic = True
print(car1)                     # <__main__.Car object at 0x00000210A673EFD0>

# collections namedtuples
from collections import namedtuple
from sys import getsizeof

Car = namedtuple('Car', ['brand', 'mileage', 'color'])
car1 = Car('bmw', 99400, "blue")
print(car1)                     # Car(brand='bmw', mileage=99400, color='blue')
print(car1.mileage)             # 99400
# car1.mileage = 89400            # AttributeError: can't set attribute

# typing.NamedTuple
from typing import NamedTuple

class Car(NamedTuple):
    brand: str
    mileage: float
    color: str

car1 = Car('bmw', 99400, "blue")
print(car1)                     # Car(brand='bmw', mileage=99400, color='blue')
print(car1.mileage)             # 99400
# car1.mileage = 89400            # AttributeError: can't set attribute

# struct.Struct
from struct import Struct
MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)
print(data)                     # b'\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00(B'
print(MyStruct.unpack(data))    # (23, False, 42.0)

# types.SimpleNamespace
from types import SimpleNamespace
car1 = SimpleNamespace(brand='bmw', mileage=99400, color='blue')
print(car1)                     # namespace(brand='bmw', mileage=99400, color='blue')
car1.mileage = 123456
print(car1.mileage)             # 123456
car1.automatic = True
del car1.color
print(car1)                     # namespace(brand='bmw', mileage=123456, automatic=True)
