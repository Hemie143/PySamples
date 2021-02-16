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

# arrays - typed arrays - mutable
import array
my_array = array.array('f', (3.14, 1.0, 3.2, 2.7))
print(my_array)                 # array('f', [3.140000104904175, 1.0, 3.200000047683716, 2.700000047683716])
print(my_array[2])              # 3.200000047683716
del my_array[2]
print(my_array)                 # array('f', [3.140000104904175, 1.0, 2.700000047683716])
my_array.append(9.5)
print(my_array)                 # array('f', [3.140000104904175, 1.0, 2.700000047683716, 9.5])
# my_array[0] = 'hello'           # TypeError

# str - immutable
array2 = 'abcdefgh'
print(array2[3])                # d
# array2[3] = 'z'                 # TypeError
# del array2[2]                   # TypeError
print(list('abcdefgh'))             # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(''.join(list('abcdefgh')))    # abcdefgh

# bytes - immutable
array3 = bytes((5, 4, 3, 2, 1))
print(array3[1])                    # 4
print(array3)                       # b'\x05\x04\x03\x02\x01'
# array3[2] = 0                       # TypeError: 'bytes' object does not support item assignment
# del array3[2]                       # TypeError: 'bytes' object doesn't support item deletion

# bytearray
array4 = bytearray((5, 4, 3, 2, 1))
print(array4[1])                    # 4
print(array4)                       # bytearray(b'\x05\x04\x03\x02\x01')
array4[2] = 0
print(array4)                       # bytearray(b'\x05\x04\x00\x02\x01')
del array4[2]
print(array4)                       # bytearray(b'\x05\x04\x02\x01')
array4.append(33)                   # integer between 0 and 256
print(array4)                       # bytearray(b'\x05\x04\x02\x01!')