x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {}
z.update(x)
z.update(y)
print(z)        # {'a': 1, 'b': 3, 'c': 4}

z = dict(x, **y)
print(z)        # {'a': 1, 'b': 3, 'c': 4}

z = dict(**x, **y)    # Python >= 3.5
# print(z)        # TypeError: type object got multiple values for keyword argument 'b'
