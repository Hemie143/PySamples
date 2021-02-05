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
print(e)
