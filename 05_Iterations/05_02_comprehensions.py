squares = [x * x for x in range(10)]
print(squares)              # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)         # [0, 4, 16, 36, 64]

# set comprehesion
set_squares = {x * x for x in range(-4, 4)}
print(set_squares)          # {0, 1, 4, 9, 16}

# dict comprehension
dict_square = {x: x * x for x in range(10)}
print(dict_square)          # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
