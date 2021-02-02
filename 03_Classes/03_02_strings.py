class Cat:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"The cat's name is {self.name} and he's got {self.color} fur"

    def __repr__(self):
        return f"Cat ({self.color}, {self.name})"

felix = Cat('black', 'Felix')
print(felix)
print(str(felix))
print(repr(felix))

import datetime
today = datetime.date.today()
print(str(today))
print(repr(today))
