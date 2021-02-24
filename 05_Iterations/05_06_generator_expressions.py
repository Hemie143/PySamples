iterator = ('Hello world' for i in range(3))

for x in iterator:
    print(x)

iterator = ('Hello world' for i in range(3))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))           # StopIteration

even_squares = (x * x for x in range(10) if x % 2 == 0)
for x in even_squares:
    print(x)

for x in ('Hello world' for i in range(3)):
    print(x)

print(sum((x * 2 for x in range(10))))

