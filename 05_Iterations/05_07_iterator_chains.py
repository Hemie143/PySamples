def integers():
    for i in range(1, 9):
        yield i

chain = integers()
print(list(chain))              # [1, 2, 3, 4, 5, 6, 7, 8]

def squared(seq):
    for i in seq:
        yield i * i

chain = squared(integers())
print(list(chain))              # [1, 4, 9, 16, 25, 36, 49, 64]

integers = range(9)
squared = (i * i for i in integers)
print(squared)                  # <generator object <genexpr> at 0x000001846C972A50>
print(list(squared))            # [0, 1, 4, 9, 16, 25, 36, 49, 64]
