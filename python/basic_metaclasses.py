from __future__ import print_function


class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return super(UpperAttrMetaclass, cls).__new__(
            cls, clsname, bases, uppercase_attr)


class Shape(object):
    __metaclass__ = UpperAttrMetaclass


class Circle(Shape):
    radius = 5


class Rectangle(Shape):
    length = 4
    height = 3


def print_attrs(cls):
    for name, item in cls.__dict__.items():
        if not name.startswith('__'):
            print(name)


def main():
    print('Circle')
    print_attrs(Circle)
    print('Rectangle')
    print_attrs(Rectangle)


if __name__ == "__main__":
    main()
