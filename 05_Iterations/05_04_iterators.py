class My_Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return My_Iterator(self)


class My_Iterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value

'''
repeat = My_Repeater('Hello world.')
for i in repeat:
    print(i)

iterator = repeat.__iter__()
while True:
    i = iterator.__next__()
    print(i)
'''

class MybetterRepeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

this_repeater = MybetterRepeater('Hello world')
for i in this_repeater:
    print(i)


class FiniteRepeater:
    def __init__(self, val, repeats):
        self.value = value
        self.repeats = repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.repeats:
            raise StopIteration
        self.count += 1
        return self.value

