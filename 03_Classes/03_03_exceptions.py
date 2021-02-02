class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError

try:
    validate('joe')
except NameTooShortError:
    print('Name too short')
