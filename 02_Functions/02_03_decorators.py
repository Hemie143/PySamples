
def null_deco(f):
    return f

@null_deco
def hello():
    return 'Hello, world!'
print(hello())

def whisper(f):
    return f().lower()

@whisper
def hello2():
    return 'Hello, world!'

print(hello2)
