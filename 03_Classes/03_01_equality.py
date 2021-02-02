# == : equality
# is : identities

a = 'foo'
b = a

print(a == b)       # True
print(a is b)       # True

c = ''.join(['f', 'o', 'o'])
print(a == c)       # True
print(a is c)       # False
