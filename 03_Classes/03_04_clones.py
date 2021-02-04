# Creating clones
new_list = list([1, 2, 3])
new_dict = dict({'a': 1, 'b': 2, 'c': 3})
new_set = set((1, 2, 3,))

# Shallow copies
x = [[1, 2], [3, 4]]
y = list(x)
print(y)                # [[1, 2], [3, 4]]
y.append([5, 6])
print(x)                # [[1, 2], [3, 4]]
print(y)                # [[1, 2], [3, 4], [5, 6]]
x[1][1] = 'Edited'
print(x)                # [[1, 2], [3, 'Edited']]           - Objects are not copied, but referenced
print(y)                # [[1, 2], [3, 'Edited'], [5, 6]]

# Deep copies
import copy
x = [[1, 2], [3, 4]]
y = copy.deepcopy(x)
print(x)                # [[1, 2], [3, 4]]
print(y)                # [[1, 2], [3, 4]]
x[1][1] = 'Edited'
print(x)                # [[1, 2], [3, 'Edited']]
print(y)                # [[1, 2], [3, 4]]

class Engine:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f"Engine {self.brand} {self.model}"


class Car:
    def __init__(self, name, motor):
        self.name = name
        self.motor = motor

    def __repr__(self):
        return f"Car ({self.name}, {self.motor})"

bmw_engine = Engine('BMW', 'S70/2')
mclaren = Car('McLaren F1', bmw_engine)
jay_car = copy.copy(mclaren)
print(mclaren)              # Car (McLaren F1, Engine BMW S70/2)
print(jay_car)              # Car (McLaren F1, Engine BMW S70/2)
print(mclaren is jay_car)   # False
jay_car.motor.model = 'S70/2 custom'
print(mclaren)              # Car (McLaren F1, Engine BMW S70/2 custom)
print(jay_car)              # Car (McLaren F1, Engine BMW S70/2 custom)
max_car = copy.deepcopy(jay_car)
max_car.motor.model = 'S70/2 enhanced'
print(mclaren)              # Car (McLaren F1, Engine BMW S70/2 custom)
print(max_car)              # Car (McLaren F1, Engine BMW S70/2 enhanced)
