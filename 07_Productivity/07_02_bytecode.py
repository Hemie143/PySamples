def greet(name):
    return f'Hello, {name}!'

print(greet('Idle'))

print(greet.__code__.co_code)           # b'd\x01|\x00\x9b\x00d\x02\x9d\x03S\x00'
print(greet.__code__.co_consts)         # (None, 'Hello, ', '!')
print(greet.__code__.co_varnames)       # ('name',)

import dis
dis.dis(greet)
