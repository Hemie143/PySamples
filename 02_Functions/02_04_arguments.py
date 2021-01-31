def foo(required, *args, **kwargs):
    # required arguments
    # positional arguments
    # keyword arguments
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo('Hello, world')
foo('Hello, world', 1, 2, 3)
foo('Hello, world', 1, 2, 3, key1='hello', key2='world')

