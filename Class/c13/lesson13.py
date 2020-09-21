# def foo():
#     x = 13
#     array = ['Lol', 'Kek']
#     k = 'testy'
#     def helloman():
#         print('Privet, Mister {}'.format(x))
#         print('Vot tvoi spisok klientov: {}'.format(array))
#         print('Vot tvoi spisok klientov: {}'.format(k))
#     return helloman
#
# bar = foo()
# bar()
# # Посмотрим какие есть атрибуты у helloman
# print(dir(bar))
# # Если мы посмотрим, то увидим, что в замыкании есть два объекта
# print(bar.__closure__)
# # Выведем их
# for attr in bar.__closure__:
#     print(attr.cell_contents)
#
# # Зададим ссылку.array2 ссылается на тот же объект в памяти?
# array2 =bar.__closure__[0].cell_contents
# # Проверим. Добавим ещё один элемент в массив и выполним функцию ещё раз.
# array2.append('Cheburek')
# bar()


# from urllib.request import urlopen
#
#
# def page(url):
#     def get():
#         return urlopen(url).read()
#
#     return get
#
#
# python = page('http://www.python.org')
# jython = page('http://www.jython.org')
# # Какой-то другой код
# # ...
# # В нужном месте вызываем
# pydata = python()
# jydata = jython()
# print(pydata[:64])
# print(jydata[:64])
# print(python.__closure__)
# print(python.__closure__[0].cell_contents)

# def countdown(n):
#    e = 0
#    def next():
#        nonlocal n, e
#        e += 1
#        r = n
#        n -= 1
#        return r
#    return next
#
# # Пример использования
# next = countdown(10)
# print(next.__closure__[0].cell_contents)
# print(next.__closure__[1].cell_contents)
# print("\n")
# while True:
#    v = next() # Получить следующее значение
#    print(v)
#    if not v: break

   # ДЕКОРАТОРЫ
"""Декораторы — это "обёртки" над функцией или классом,
которые дают нам возможность изменить поведение функции, не изменяя её код."""

"""@trace
def square(x):
   return x * x


def square(x):
   return x * x

square = trace(square)"""

#
# def some_decorator(func):
#    def dop_func():
#        print("Do something before")
#        func()
#        print("Do something after")
#    return dop_func
#
#
# def some_decorator2(func):
#    def dop_func(*args):
#        print("Do something")
#        return func(*args)
#    return dop_func
#
# @some_decorator
# def show_some():
#    print("Hello!")
#
#
# @some_decorator2
# def pow(x, val):
#    return x ** val
#
# show_some()
# print(pow(2, 4))
# print(pow(3, 3))

# ДЕКОРАТОРЫ (ПРИМЕР 3) - ДЕКОРАТОР В ВИДЕ КЛАССА
# Очень редкая ситуация. Обычно, проще воспользоваться механизмом замыкания, но и такая возможность есть.

# class Log():
#    def __init__(self):
#        pass
#
#    # Магический метод __call__ позволяет обращаться к
#    # объекту класса, как к функции
#    def __call__(self, func):
#        def decorated(*args, **kwargs):
#            res = func(*args, **kwargs)
#            print('log: {}({}, {}) = {}'.format(func.__name__, args, kwargs, res))
#            return res
#        return decorated
#
# @Log()
# def square(x):
#    return x*x
#
# square(4)


# def makebold(fn):
#    def wrapped():
#        return "<b>" + fn() + "</b>"
#    return wrapped
#
# def makeitalic(fn):
#    def wrapped():
#        return "<i>" + fn() + "</i>"
#    return wrapped
#
# @makebold
# @makeitalic
# def hello_with_dec():
#    return "Hello decorators!"
#
# def hello_simple():
#    return "Hello decorators!"
#
# print(hello_with_dec())
#
# # Добьемся аналогичного результата
# hello_simple = makebold(makeitalic(hello_simple))
# print(hello_simple())

# def documentirovanie(n):
#    """ Вычисляет факториал числа. Например:
#        >>> factorial(6)
#        720
#    """
#    if n <= 1:
#        return 1
#    else:
#        return  n * factorial(n-1)
#
# print(documentirovanie.__doc__)

# def wrap(func):
#    def call(n):
#        return func(n)
#
#    call.__doc__ = func.__doc__
#    call.__name__ = func.__name__
#    return call
#
# @wrap
# def factorial(n):
#    """ Вычисляет факториал числа. Например:
#        >>> factorial(6)
#        720
#    """
#    if n <= 1:
#        return 1
#    else:
#        return  n * factorial(n-1)
#
# print(factorial.__doc__)
# print(factorial.__name__)

registry = []  # (1)


# def register(func):  # (2)
#    print("running register(%s)" % func)  # (3)
#    registry.append(func)  # (4)
#    return func  # (5)
#
# @register  # (6)
# def f1():
#    print("running f1()")
#
# @register
# def f2():
#    print("running f2()")
#
# def f3():  # (7)
#    print("running f3()")
#
# def main():  # (8)
#    print("running main()")
#    print("registry ->", registry)
#    f1()
#    f2()
#    f3()

#
# from functools import wraps
#
#
# def repeat(n=5):
#     def _repeat(f):
#         @wraps(f)
#         def inner(*args, **kwargs):
#             for _ in range(n):
#                 f(*args, **kwargs)
#         return inner
#     # не забываем ее вернуть!
#     return _repeat
#
#
# @repeat(3)
# def foo(test):
#     print(f'hello {test}')
# (foo('test'))

#
# registry = {}
#
# def register(cls):
#    registry[cls.__clsid__] = cls
#    return cls
#
# @register
# class Foo:
#    __clsid__ = "007"
#
#    def bar(self):
#        pass
#
# foo = Foo
# print(registry)
#
#
# registry = {}
#
# def register(change_id=False):
#    def wrap(cls):
#        if change_id:
#            cls.__clsid__= "00{}".format(str(int(cls.__clsid__[-1]) + 1))
#        registry[cls.__clsid__] = cls
#        return cls
#    return wrap
#
# @register(True)
# class Foo:
#    __clsid__ = "007"
#
#    def bar(self):
#        pass
#
# foo = Foo()
# print(foo.__clsid__)
# print(registry)

import logging
logging.basicConfig(
   filename = "app.log",
   format = "%(levelname)-10s %(asctime)s %(message)s",
   level = logging.INFO
)
log = logging.getLogger("app")
# Записать сообщение, используя позиционные аргументы форматирования
host = 'localhost'
port = 7777
log.critical("Can't connect to %s at port %d", host, port)
# Записать сообщение, используя словарь значений
parms = { 'host' : 'www.python.org',
'port' : 80
}
log.critical("Can't connect to %(host)s at port %(port)d", parms)