students = {
    'Alice': 19,
    'Bob': 18,
    'Charlie': 20,
}
print(students['Bob'])      # 18

cubes = {x: x * x * x for x in range(10)}
print(cubes)                # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}

# OrderedDict
import collections
d = collections.OrderedDict(one=1, two=2, three=3)
print(d)                    # OrderedDict([('one', 1), ('two', 2), ('three', 3)])
print(d.keys())             # odict_keys(['one', 'two', 'three'])

# defaultdict
e = collections.defaultdict(list)
print(e)                    # defaultdict(<class 'list'>, {})
e['cats'].append('Felix')
e['cats'].append('Milo')
print(e)                    # defaultdict(<class 'list'>, {'cats': ['Felix', 'Milo']})
print(e['dogs'])            # []

# ChainMap
dict1 = {1: 'one', 2: 'two'}
dict2 = {3: 'three', 4: 'four', 'hello': 'world'}
f = collections.ChainMap(dict1, dict2)
print(f)                    # ChainMap({1: 'one', 2: 'two'}, {3: 'three', 4: 'four'})
print(f['hello'])           # world

# MappingProxyType
from types import MappingProxyType
my_dict = {'alice': 19, 'bob': 18, 'charlie': 20}
read_only = MappingProxyType(my_dict)
print(read_only)            # {'alice': 19, 'bob': 18, 'charlie': 20}
# read_only['bob': 21]        # TypeError
my_dict['bob'] = 21
print(read_only)            # {'alice': 19, 'bob': 21, 'charlie': 20}
