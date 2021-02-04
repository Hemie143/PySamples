from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class MyClass(Base):
    def foo(self):
        pass

assert issubclass(MyClass, Base)
m = MyClass()                       # TypeError: Can't instantiate abstract class MyClass with abstract methods bar

