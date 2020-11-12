# ПОЛИМОРФИЗМ
# super().__init__()


# вызов метода от родительского класса

# Применение полиморфизма
# --- > НАЧАЛО
class Transport:
    __type = "default"
    def __init__(self, params="default"):
        """Какой-то конструктор
           :param params: возможно, с каким-то параметором
           """
        pass
    def move(self):
        print("Я транспорт типа: {}. Я умею перемещаться".format(self.__type))
# polimorfism(transportDefault)
# polimorfism(car)

class Car(Transport):
    __type = "car"
    def __init__(self, model, maxSpeed):
        super().__init__()
        self.model = model
        self.maxSpeed = maxSpeed
    def move(self):
        print("Я транспорт типа: {}. Модель: {}."
              "Я могу ехать со скоростью {} км/ч"
              .format(self.__type, self.model, self.maxSpeed))


transportDefault = Transport()
car = Car("Tesla model X", 440)

def polimorfism(transport):
    if hasattr (transport, 'move'): #hasattr - проверяет у объекта есть ли заданный атрибут 'move'
        transport.move()
    else:
        print('я не знаю move')


polimorfism(transportDefault)
polimorfism(car)
car.move()
# КОНЕЦ '''

# ПЕРЕГРУЗКА ОПЕРАТОРОВ

''' ---> BEGIN
class Vector:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    #перегружаем оператор +
    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))
    def as_point(self):
        return self.x, self.y

    #формируем удобное отображение объекта при выводе функции print()
    def __str__(self):
        return "V(x: {} y: {})".format(self.x,self.y)

#создаем ээкземпляры класса (объекты)
v1 = Vector((10,15))
v2 = Vector((12,10))
v4 = Vector((15,9))
#наши объекты учавствуют в операции сложения (+)
v3 = v1 + v2 + v4
#на самомделе это работает так:
#v3 = v1.__add__(v2)
#Благодаря перезагрузке мы можем использовать более удобную и привычную запись:
#v3 = v1 + v2
print(v3)
---> END'''

# ИНТЕРФЕЙС ИТЕРАЦИЙ
''' ---> BEGIN
class IterObj:
    """
    Объект итератор
    """

    def __init__(self, start=0):
        self.i = start

        # Объект считается итератором - если у него есть метод __next__

    def __next__(self):
        self.i += 1
        if self.i <= 9:
            return self.i
        else:
            raise StopIteration


class Iter:
    """
    Объект, поддерживающий интерфейс операции
    """

    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        return IterObj(self.start)

obj = IterObj(2)
x = [1,2,3]
# obj = Iter(start=2)
# for el in obj:
#     print(el)
# print("Еще раз...")
# for el in obj:
#     print(el)
# print("sum(obj) -- >", sum(obj))
# # функция map() возвращает объект-итератор
# map_iter = map(int, '123')
# print('next(map_iter) -->', next(map_iter))
# print('next(map_iter) -->', next(map_iter))
# # Цикл for in родолжает перебор элементов, т.к. map_iter является итератором
# # for el in map_iter:
#     print("el in for in -->", el)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
---> END'''

''' ---> BEGIN
class Iter2:
    def __init__(self, start=0):
        self.i = start
    def __iter__(self):
# метод __iter__ должен возвращать объект итератор
        return self
    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration
print('Demo Iter2')
obj = Iter2(start=2)
for el in  obj:
    print(el)
print('Еще раз ...')
for el in obj:
    print(el) ---> END'''

# "@property - позволяет обращаться к методу как к атрибуту

# class Student(Person):
#     def __init__(self, name, surname, age, school, class_room):
#         Person.__init__(self, name, surname, age, school)
#         self._class_room = class_room
#
#     @property
#     def set_new_class_room(self, class_room):
#         self._class_room = class_room
#
# student_1 = Student("Maks", "Russol", "22", "school", "2d")
# student_1 = Student("Vania", "Ivanov", "23", "school", "2d")
# student_1 = Student("Lesha", "Petrov", "24", "school", "2d")
# student_1 = Student("Kuzia", "QWER", "21", "school", "2d")


''' ---> BEGIN
# Расширяем стандартный класс дикт
class my_dict(dict):
    # Добавляем свой метод
    def new_method(self):
        return "I'm new method"
    @staticmethod
    def test_method():
        return "test"
    # Добавляем дополнительный функционал к существующему
    def __setitem__(self, key, value):
        print('Setting %r to %r' % (key, value))
        return super().__setitem__(key, value)


# m_dict = my_dict({1: 2, 2: 3})
# # Данная операция вызывает метод __сэтитем__
# m_dict["new key"] = "new_value"
# print(m_dict)
# print(m_dict.keys())
# print(m_dict.new_method())
print(my_dict.test_method())
---> END'''

#
# class MyList(list):
#     """
#     Список - индексы которого начинаются с 1, а не с 0
#     """
#
#     def __getitem__(self, offset):
#         print('(Indexing % s at % s)' % (self, offset))
#         return list.__getitem__(self, offset - 1)
#
#
# x = MyList('abc')  # __init__ наследуется из списка
# print(x)  # __repr__ наследуется из списка
# print(x[1])  # My.List__getitem__
# print(x[3])  # Изменяет поведение метода суперкласса
# x.append('spam')
# print(x)  # Атрибуты, унаследованные от суперкласса лисьт
# x.reverse()
# print(x)
