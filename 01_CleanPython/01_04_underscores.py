# single leading underscore
# convention: used for internal/private use, shouldn't be used from external module
# this convention isn't enforced
_foo = 'hello_world'

# This method won't be export with a wildcard import
# from 01_04_underscores import * # Won't work because of invalid decimal literal
def _internal_func():
    print('Hello world')

# single trailing underscore
# convention: used to avoid using a reserved keyword
class_ = 'this is my class'

# double leading underscores
# used to avoid naming conflicts between a class and its subclasses, for methods and variables
class foo:
    def __init__(self):
        self.__prop1 = 10

class bar(foo):
    def __init__(self):
        self.__prop1 = 20

f = foo()       # Contains no value "__prop1", contains "_foo__prop1"
b = bar()       # Contains no value "__prop1", contains "_bar__prop1"
print(b._bar__prop1)

# double leading and trailing underscores
# reserved for special use
class foobar:
    def __init__(self):
        self.__foo__ = 10

# single underscore
# temporary value, placeholder, result of last operation
for _ in range(10):
    print('Hello world')

myvar = 'hello'
print(_)
