from __future__ import print_function


class SimpleAttrMetaclass(type):
    def __new__(cls, clsname, bases, dct):
        obj_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                obj_attr[name] = val

        def obj_init(obj):
            for name, val in obj_attr.items():
                obj.__dict__[name] = val

        def print_obj_attrs(obj):
            lines = []
            lines.append(obj.__class__.__name__)
            for name, val in obj.__dict__.items():
                lines.append('name = {}, value = {}'.format(name, val))
            return '\n'.join(lines)

        attr = {'__init__': obj_init, '__repr__': print_obj_attrs}
        return super(SimpleAttrMetaclass, cls).__new__(
            cls, clsname, bases, attr)


class Shape(object):
    __metaclass__ = SimpleAttrMetaclass


class ShapeSimple(object):
    def __repr__(self):
        lines = []
        lines.append(self.__class__.__name__)
        for name, val in self.__dict__.items():
            lines.append('name = {}, value = {}'.format(name, val))
        return '\n'.join(lines)


class CircleSimple(ShapeSimple):
    def __init__(self):
        self.radius = 5


class RectangleSimple(ShapeSimple):
    def __init__(self):
        self.length = 4
        self.height = 3


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

    c = Circle()
    print(c)
    r = Rectangle()
    print(r)

    c = CircleSimple()
    print(c)
    r = RectangleSimple()
    print(r)


if __name__ == "__main__":
    main()
