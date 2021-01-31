def print_coord(x, y, z):
    print(f'x:{x} - y:{y} - z:{z}')

coord1 = (1, 2, 3)
coord2 = [4, 5, 6]
print_coord(*coord1)
print_coord(*coord2)

coord_dict = {'z': 9, 'x': 7, 'y': 8}
print_coord(**coord_dict)
