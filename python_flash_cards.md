---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

Q01. Strings: split join

```python
str = 'lock stock barrel'
words = str.split(' ')
words
# ['lock', 'stock', 'barrel']
', '.join(words)
# ['lock', 'stock', 'barrel']
```

Q02. Regular expressions

```python
'''
('ab*', 'a followed by zero or more b'),
('ab+', 'a followed by one or more b'),
('ab?', 'a followed by zero or one b'),
('ab{3}', 'a followed by three b'),
('ab{2,3}', 'a followed by two to three b')
'''

import re
text = 'abbaaabbbbaaaaa'
pat = 'ab'  # pattern

for match in re.finditer(pat, text):
    s = match.start()
    e = match.end()
    print('{!r} at {:d}:{:d}'.format(
        text[s:e], s, e))
# 'ab' at 0:2
# 'ab' at 5:7
```

Q03. Enumerations

```python
import enum

class BugStatus(enum.Enum):
    new = 3
    invalid = 2
    wont_fix = 1

[(st.name, st.value) for st in BugStatus]

# TypeError: '<' not supported between
# instances of 'BugStatus' and 'BugStatus'
# [st.value for st in sorted(BugStatus)]

class BugStatusInt(enum.IntEnum):
    new = 3
    invalid = 2
    wont_fix = 1

# works fine
[st.value for st in sorted(BugStatusInt)]

# dynamically create enum
BugStatus = enum.Enum(
    value='BugStatus',
    names=('wont_fix closed new'))

[(st.name, st.value) for st in BugStatus]
# [('wont_fix', 1), ('closed', 2), ('new', 3)]
```

Q04. Collections - ChainMap

```python
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

# search through dictionaries
# in order
m = collections.ChainMap(a, b)

[(k, v) for k, v in m.items()]
# [('c', 'C'), ('b', 'B'), ('a', 'A')]
```

Q05. Collections - Counter

```python
from collections import Counter
c = Counter('store')
print(c)
# Counter({'s': 1, 't': 1, 'o': 1, 'r': 1, 'e': 1})
c + Counter('toe')
# Counter({'s': 1, 't': 2, 'o': 2, 'r': 1, 'e': 2})
```

Q06. Collections - defaultdict

```python
from collections import defaultdict

s = [('red', 1), ('blue', 1), ('red', 2)]
d_list = defaultdict(list)
for k, v in s:
    d_list[k].append(v)
print(d_list)
# defaultdict(<class 'list'>, {'red': [1, 2], 'blue': [1]})
d_count = defaultdict(int)
for k, v in s:
    d_count[k] += v
print(d_count)
# defaultdict(<class 'int'>, {'red': 3, 'blue': 1})
```

Q07. Collections - deque

```python
from collections import deque

d = collections.deque('hel')
d.append('l')
print(d)  # deque(['h', 'e', 'l', 'l'])
d.appendleft('s')
print(d)  # deque(['s', 'h', 'e', 'l', 'l'])
d.popleft()
print(d)  # deque(['h', 'e', 'l', 'l'])
d.pop()
print(d)  # deque(['h', 'e', 'l'])
```

Q08. Collections - namedtuple

```python
from collections import namedtuple

Person = namedtuple('Person', 'name age')
rob = Person(name='Rob', age=12)
print(rob)  # Person(name='Rob', age=12)
print(rob.name, rob.age)  # Rob 12
[item for item in rob]  # ['Rob', 12]
```

Q09. heapq - binary min-heap

```python
import heapq
# heapq implements a binary heap that works
# with lists and implements min-heap where
# parent <= both children
# children of node N is at 2 * N + 1, 2 * N + 2
data = '43521'
l = []
for item in data:
    heapq.heappush(l, item)
    print(l)
# ['4']
# ['3', '4']
# ['3', '4', '5']
# ['2', '3', '5', '4']
# ['1', '2', '5', '4', '3']
```

Q10. bisect

```python
import bisect
# bisect maintains lists in sorted order
data = '43521'
l = []
for item in data:
    bisect.insort(l, item)
    print(l)
# ['4']
# ['3', '4']
# ['3', '4', '5']
# ['2', '3', '4', '5']
# ['1', '2', '3', '4', '5']
```

Q11. queue

```python
import queue

q_fifo = queue.Queue()
q_lifo = queue.LifoQueue()

for i in range(5):
    q_fifo.put(i)
    q_lifo.put(i)

while not q_fifo.empty():
    print(q_fifo.get(), end=' ')
print()

while not q_lifo.empty():
    print(q_lifo.get(), end=' ')
    
# 0 1 2 3 4
# 4 3 2 1 0
```

Q12. copy

```python
import copy
a = [2, 3]
a_copy = copy.copy([1, a])
print(a_copy[1] is a)  # True

a_deepcopy = copy.deepcopy([1, a])
print(a_deepcopy[1] is a)  # False
```

Q13. functools

```python
from functools import partial
int('10', base=2), int('10')
# (2, 10)

int_2 = partial(int, base=2)
int_2('10')
# 2

from functools import reduce
reduce(lambda x, y: x+y, [1, 2, 3])
# 6

from functools import singledispatch

# different function called based on type
@singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))

@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))

@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list({})'.format(arg))

myfunc(3)
myfunc([1, 2])
myfunc('abc')

# myfunc_int(3)
# myfunc_list([1, 2])
# default myfunc('abc'
```

Q14. itertools

```python
from itertools import *
import operator
# count(10) --> 10 11 12 ...
# cycle('AB') --> A B A B
# repeat(10, 3) --> 10 10 10
# accumulate([1, 2, 3], operator.add)
# 1 3 5

# chain('AB', 'CDE') --> A B C D E
# compress('ABC', [1, 0, 1]) --> A C
# dropwhile(lambda x: x < 5, [1, 6]) --> 6
# takewhile(lambda x: x < 5, [1, 6]) --> 1
# filter(lambda x: x % 2, range(3)) --> 1
# filterfalse(lambda x: x % 2, range(3)) --> 0 2
# islice('ABCDE', 1, 4, 2) --> B D
# starmap(pow, [(2,5), (3,2)]) --> 32 9

# [k for k, g in groupby('AABBBC')] --> A B C
# [list(g) for k, g in groupby('AABBBC')] --> AA BBB C

product('ABC', repeat=2)
# AA AB AC BA BB BC CA CB CC

permutations('ABC', 2)
# AB AC BA BC CA CB

combinations('ABC', 2)  # AB AC BC
```

Q15. contextlib

```python
class WithinContext:
    def do_something(self):
        print('  WithinContext.do_something()')

class Context:
    def __init__(self):
        print('__init__()')
    def __enter__(self):
        print('Context.__enter__()')
        return WithinContext()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit__()')

with Context() as d:
    d.do_something()
    
# Context Managers as Function Decorators
import contextlib

class Context(contextlib.ContextDecorator):
    def __init__(self, how_used):
        self.how_used = how_used
        print('__init__({})'.format(how_used))
    def __enter__(self):
        print('__enter__({})'.format(self.how_used))
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({})'.format(self.how_used))

@Context('as decorator')
def func(message):
    print(message)

with Context('as context manager'):
    print('Doing work in the context')

func('Doing work in the wrapped function')

# Generators as context managers
@contextlib.contextmanager
def make_context():
    print('entering')
    try:
        yield {}
    finally:
        print('exiting')

with make_context() as value:
    print('inside with statement:', value)
```

Q16. decorators

```python
def print_log1(f):
    def inner(*args, **kwargs):
        print('in function:', f.__name__)
        return f(*args, **kwargs)
    return inner

@print_log1
def add1(x, y):
    print(x + y)
    
add1(3, 4)
# in function: add1
# 7

def print_log2(message):
    def decorator(f):
        def inner(*args, **kwargs):
            print('in function:', f.__name__, message)
            return f(*args, **kwargs)
        return inner
    return decorator

@print_log2('trace')
def add2(x, y):
    print(x + y)
    
add2(3, 4)
# in function: add2 trace
# 7
```

Q17. Generators

```python
# generator defined using a function
def seq(n):
    for i in range(n):
        yield i

# using a generator
list(seq(3))
# [0, 1, 2]

# generator expression
list(i for i in range(3))
# [0, 1, 2]

gen = seq(3)
next(gen)  # 0
next(gen)  # 1
next(gen)  # 2

# using a class
class Seq:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.val = 0
        return self
    def __next__(self):
        if self.val >= self.n:
            raise StopIteration

        result = self.val
        self.val += 1
        return result
```

Q18. Asyncio

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    # sequential
    await say_after(1, 'wait_1')
    await say_after(2, 'wait_2')
    print(f"finished at {time.strftime('%X')}")
    # in parallel
    await asyncio.gather(
        say_after(1, 'wait_1'), say_after(2, 'wait_2'))
    print(f"finished at {time.strftime('%X')}")

# Python 3.7
# asyncio.run(main())

# Before Python 3.7
loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
```

Q19. Metaclasses

```python
class Meta(type):
    def __init__(cls, name, bases, dct):
        for attr in dct['attrs']:
            setattr(cls, attr, 0)
        delattr(cls, 'attrs')

class Square(metaclass=Meta):
    attrs = ['height', 'width']

s = Square()
# print all the object attributes
print([attr for attr in dir(s) if not attr.startswith('_')])
# ['height', 'width']
```

Q20. Class properties

```python
class Circle:
    def __init__(self):
        self._radius = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

c = Circle()
c.radius = 3  # setter called
r = c.radius    # getter called
del c.radius      # deleter called
```

Q21. classmethod and staticmethod

```python
class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def foo(self, x):
        print("run foo({}, {})".format(self, x))

    @classmethod
    def class_foo(cls, x):
        print("run class_foo({}, {})".format(cls, x))

    @staticmethod
    def static_foo(x):
        print("run static_foo({})".format(x))

b = Box(3, 4)
b.foo(5)
Box.class_foo(5)
Box.static_foo(5)
# run foo(<__main__.Box object at 0x7f042677df60>, 5)
# run class_foo(<class '__main__.Box'>, 5)
# run static_foo(5)
```
