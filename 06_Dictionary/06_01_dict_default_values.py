students = {
    473: 'Alice',
    592: 'Bob',
    243: 'Charlie',
}

def greet(id):
    return f'Hello, {students[id]} !'

print(greet(473))           # Hello, Alice !
# print(greet(1))             # KeyError: 1

def greet(id):
    try:
        return f'Hello, {students[id]} !'
    except KeyError:
        return 'Hello, there!'

print(greet(473))           # Hello, Alice !
print(greet(1))             # Hello, there!

def greet(id):
    return f'Hello, {students.get(id, "there")} !'

print(greet(473))           # Hello, Alice !
print(greet(1))             # Hello, there!
