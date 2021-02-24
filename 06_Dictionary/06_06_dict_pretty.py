my_dict = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(my_dict)          # {'a': 23, 'b': 42, 'c': 12648430}
print(str(my_dict))     # {'a': 23, 'b': 42, 'c': 12648430}

import json
print(json.dumps(my_dict, indent=4, sort_keys=True))
# Only works with keys as strings
'''
{
    "a": 23,
    "b": 42,
    "c": 12648430
}'''

import pprint
pprint.pprint(my_dict)  # {'a': 23, 'b': 42, 'c': 12648430}

