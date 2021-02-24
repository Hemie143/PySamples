# Infinite generator
def repeater(value):
    while True:
        yield value

def limited_repeater(value, repeats):
    count = 0
    while True:
        if count > repeats:
            return
        count += 1
        yield value

def limited_repeater2(value, repeats):
    for _ in range(repeats):
        yield value