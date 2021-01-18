# single leading underscore
# convention: used for internal/private use, shouldn't be used from external module
# this convention isn't enforced
_foo = 'hello_world'

# This method won't be export with a wildcard import
from 01_04_underscores import *
def _internal_func():
    print('Hello world')

# single trailing underscore
# convention: used to avoid using a reserved keyword
class_ = 'this is my class'

# double leading underscore
