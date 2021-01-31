def foo(x):
    if x:
        return x
    else:
        return None

def bar(x):
    if x:
        return x
    else:
        return          # equivalent to return None

def foorbar(x):
    if x:
        return x
    # Implicit return None
