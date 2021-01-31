
def shout(text):
    return text.upper()

# Functions are first-class objects
# Functions can be assigned to variables
scream = shout
print(scream('Hello'))
print(scream.__name__)      # shout

# Functions can be stored in data structures
my_funcs = [scream, str.capitalize, str.upper, str.lower]
print(my_funcs)
for f in my_funcs:
    print(f('Hello'))

# Functions can be passed in arguments
def hello(func):
    result = func('Saying hello')
    print(result)

def whisper(text):
    return text.lower()

hello(scream)
hello(whisper)
print(list(map(scream, ['text1', 'text2', 'text3'])))

# Nested functions
def speak(text):
    def murmur(t):
        return t.lower()
    return murmur(text)
print(speak('Hello - nested'))

# Return a function
def choose_func(volume):
    def murmur(t):
        return t.lower()
    def shout(t):
        return t.upper()
    return shout if volume > 0.5 else murmur

print(choose_func(0.4))
print(choose_func(0.6))
print(choose_func(0.4)('Hello'))

# Closure
def choose_func_closure(text, volume):
    def murmur():
        return text.lower()
    def shout():
        return text.upper()
    return shout if volume > 0.5 else murmur

print(choose_func_closure('Hello closure', 0.6)())

def apply_discount(d):
    def apply(x):
        return x * (1 - d / 100)
    return apply

discount_10 = apply_discount(10)
discount_20 = apply_discount(20)

print(discount_10(120))
print(discount_20(120))

# callable
class Discount:
    def __init__(self, d):
        self.discount = d

    def __call__(self, x):
        return x * (1 - self.discount / 100)

discount_15 = Discount(15)
print(discount_15(120))




