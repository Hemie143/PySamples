
class Cat:
    num_legs = 4

    def __init__(self, name):
        self.name = name

felix = Cat('Felix')
print(felix.name)           # Felix
print(felix.num_legs)       # 4
print(Cat.num_legs)         # 4

Cat.num_legs = 5
print(felix.num_legs)       # 5
felix.num_legs = 4
print(felix.num_legs)       # 4

class CountCats:
    num_cats = 0

    def __init__(self, name):
        self.name = name
        self.__class__.num_cats += 1

print(CountCats('Felix').num_cats)          # 1
print(CountCats('Sheby').num_cats)          # 2
