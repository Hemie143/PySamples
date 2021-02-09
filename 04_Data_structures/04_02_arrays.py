# Lists - mutable
my_list = ['alice', 'bob', 'charlie']
print(my_list[0])           # alice
my_list[1] = 'bill'
print(my_list)              # ['alice', 'bill', 'charlie']
del my_list[1]
print(my_list)              # ['alice', 'bill']
my_list.append(3.14)
print(my_list)              # ['alice', 'bill', 3.14]

# tuples - immutables
my_tuple = ('alice', 'bob', 'charlie')
print(my_tuple[0])
# my_tuple[1] = 'bill'        # TypeError
# del my_tuple[1]             # TypeError

# arrays - typed arrays

