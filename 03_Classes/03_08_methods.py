class Foo:
    def instance_method(self):
        return f'instance method: {self}'

    @classmethod
    def class_method(cls):
        return f'class method: {cls}'

    @staticmethod
    def static_method():
        return f'static method: ??'

foo= Foo()
print(foo.instance_method())
print(foo.class_method())
print(foo.static_method())

print(Foo.class_method())
print(Foo.static_method())