'''
Syntax:
statement = assert expression1 ["," expression2]

Tips:
1. Not used for data validation, as it can be by-passed if the code is optimized by the interpreter
2. Used for debugging only, don't rely on it for run-time
2. No parenthesis
'''

def set_discount(item, discount):
    price = int(item['price'] * (1.0 - discount))
    assert 0 <= price <= item['price']
    return price

item_sample = {'name': 'Acme item', 'price': 150}
print(set_discount(item_sample, 0.15))
print(set_discount(item_sample, 1.15))          # generates an AssertionError

