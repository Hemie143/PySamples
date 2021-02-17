# set
vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels)                       # {'a', 'u', 'o', 'i', 'e'}
print('o' in vowels)                # True
name = set('alice')
print(name.intersection(vowels))    # {'a', 'e', 'i'}
vowels.add('y')
print(vowels)                       # {'y', 'o', 'a', 'e', 'u', 'i'}

# frozenset
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
# vowels.add('y')                     # AttributeError: 'frozenset' object has no attribute 'add'
d = { frozenset({1, 2}) : 'hello'}  # dictionary
print(d)                            # {frozenset({1, 2}): 'hello'}

# collections.Counter
from collections import Counter
garage = Counter()
car1 = {'brand': 'bmw', 'mileage': 99400}
garage.update(car1)
print(garage)                       # Counter({'brand': 'bmw', 'mileage': 99400})

