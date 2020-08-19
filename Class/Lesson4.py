# Встроенные функци Ч.1
for i in range(1,8,2): #range (1,2,3) 1-начало 2-конец 3-шаг
    print(i)

print(abs(-2)) # - Возвращает абсолютную величину (модуль числа).
print (max (1,2,3,4,5,6,7)) # - Максимальный элемент последовательности.
min(1,2,3,4,5,6,7) # - Минимальный элемент последовательности.


x = round (2.34534545,3) # round (X,N )Округление X значения до N знаков после запятой.
print(x)

y = sum(2.56, 1, 12) # sum (iter,start=0) С- умма членов последовательности.

z = type([]) # type(object)- Возвращает тип объекта.
print(type(z))

d = [1,2,3,4,5]
for i,y in enumerate(d): #- Возвращает пары,(элемент, его индекс) только для последовательностей
    print(i,y)
'''
def summ (a,b):

    # :param a:
    # :param b: #документирование функции
    # :param c:

    return a+b
x=5
y=6
s = summ(x,y)
print(s)

# LAMBDA-ФУНКЦИИ
# Анонимные (lambda) функции могут содержать лишь одно выражение, но и выполняются они быстрее.
# Анонимные функции создаются с помощью инструкции lambda. Кроме этого, их не обязательно присваивать переменной.
f = lambda x: x ** 2
print (f(4))
print ((lambda x:x**2)(4)) '''

#     # Практика области видимости:
# x = 5
# def outside():
#     y=10
#     def inside():
#         z=15
#         print(f'inside:{x},{y},{z}')
#         inside()
#         print(f'outside {x},{y}, z недоступна')
#     outside()
#     print(f'inside {x}, y недоступна, z недоступна')
#
# x=5
# def wrapper ():
#     def test1():
#         x=10 #локальная переменная х перекрывает видимость глобальной х
#         print('test1 x= ', x)
#     def test2():
#         print('test2 x= ', x)
# #ошибка х = 22#
#     def test3():
#         global x
#         print('test3 x =', x)
#         x=25
#     test1()
#     test2()
#     test3()
# wrapper()
# print('after wrapper x = ', x)

# ПРОИЗВОЛЬНОЕ КОЛИЧЕСТВО АРГУМЕНТОВ В ФУНКЦИИ
# Для получения неопределенного (любого) количества аргументов используют конструкцию: *args в качестве параметра функции, где args–произвольное имя.

# def average (*args):
#     summ = 0
#     for arg in args:
#         summ += arg
#     return summ/len(args)
# print (round(average(1,2,3)))
#
# #ИМЕНОВАННЫЕ АРГУМЕНТЫ
#
# def print_into(**kwargs):
#     print("You name is %s %s. You age is %s. And your address is: %s"%(kwargs["name"],kwargs["surename"],kwargs["age"], kwargs["adress"]))
# print_into(name = "Максим", surename = "Руссол", age = "29", adress = "ул. Революционная, 56")
#
# def print_into_2(**kwargs):
#     print(f'You name {name}. You age is {age}. And your address is: {adress}')
#     print_into_2(name= "Максим", surename= "Руссол", age= "29", adress= "ул. Революционная, 56")

def welcome (name='Инкогнито'):
    print(f'Privet, {name}')
welcome('User')
welcome()

#ВСТРОЕННЫЕ ФУНКЦИИ (ЧАСТЬ 2)

# zip() - итератор, который генерирует серию множеств, содержащие элементы из каждой итерации

a = [1,2]
b = [3,5,6,7]
c = [3,5,6]
print(zip(a,b,c))
for i in zip (a,b,c):
    print (i)

# map() - итератор, каждым элементом которого является применение функции funk_link к элементам исходного итератора
#результат оборачиваем в list чтобы увидеть полный результат

print(list(map(lambda x: x*x, [2,5,12,-2])))

print(list(map(len, ['21','122','2222222','22222']))) # количество символов (длина0 каждого элемента объекта мар [2, 3, 7, 5]

# filter () - тбрасывает те элементы, для которых функция возвращает False
print(list(filter(len, ['','not null','bla','','10']))) #отбрасывает все элементы с длитной НОЛЬ

#РАБОТА С ФАЙЛАМИ

# import os
# path = os.path.join('russol.txt')
# f = open(path, 'r', encoding= 'UTF-8')
# print(f.readlines())
# f.close()
#
#
# path = os.path.join('russol.txt')
# f = open(path, 'r', encoding= 'UTF-8')
# wanted_symbol = 'f'
# for line in f:
#     if wanted_symbol in line:
#         print (line)
#         break

my_file = open('russol.txt', 'w')
my_file.write('Python nice')
my_file.close()