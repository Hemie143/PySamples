# Typical use of context manager, where closure is guaranteed
with open('hello_world.txt') as f:
    out = f.readlines()

# Wrong implementation of opening a file
f = open('hello_world.txt')
out = f.readlines()
f.close()               # Will not be executed if an error happens on line above

# Creating own custom context managers
# Create a class with methods __enter__ and __exit__
class MyResource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Alternate solution is to use contextlin
from contextlib import contextmanager

@contextmanager
def resource(name):
    try:
        f = open(name, "r")
        yield f             # Generator
    finally:
        f.close()

with resource('hello_world.txt') as f:
    out = f.readlines()
