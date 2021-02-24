my_dict = {'a': 5, 'c': 2, 'b': 3, 'd': 1}

print(sorted(my_dict.items()))                                      # [('a', 5), ('b', 3), ('c', 2), ('d', 1)]
print(sorted(my_dict.items(), key=lambda x: x[1]))                  # [('d', 1), ('c', 2), ('b', 3), ('a', 5)]

import operator
print(sorted(my_dict.items(), key=operator.itemgetter(1)))          # [('d', 1), ('c', 2), ('b', 3), ('a', 5)]
print(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))    # [('a', 5), ('b', 3), ('c', 2), ('d', 1)]
