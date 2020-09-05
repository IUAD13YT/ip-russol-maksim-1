# n1 = 2
# n2 = n1
# n1 = 4
# # Неизменяемые объекты int, float, complex, str, tuple - Immutable objects
# # Изменяемые объекты set, list, dict - Mutable objects
# print(f'n1={n1} n2={n2}')

# sp1 = [1, 2, 3]
# sp2 = sp1
# sp2.append(4)
# print("sp1 =", sp1, "sp2 =", sp2)
# print(f'id(sp1) = {id(sp1)} id(sp2) = {id(sp2)}')

# def modify(lst):
#     lst.append("new")
#     return lst
# my_list = [1,2,3]
# mod_list = modify(my_list[:])
# # Функция вернула измененный список
# print('mod_list =', mod_list, id(mod_list))
# # Но исходный список тоже изменился, подобное неявное поведение нежелательно для функций
# print('my_list', my_list, id(my_list))


# my_list = [1, -2, -4, 0, 5, -2]
# # Удаляем все отрицательные элементы
# for el in list(my_list):
#     if el < 0:
#         my_list.remove(el)
# print("1)my_list after remove -->", my_list)
# Если нужно сделать полную копию со всеми вложенными изменяемыми объектами,
# используем copy
import copy
sp = [[2,3], [4,6,[7,8]]]
sp_copy = copy.deepcopy(sp)
sp_copy = sp[:] #list(sp)
print('sp',sp)
print('sp_copy',sp_copy)
sp[0].append(10)
sp_copy[1].append(20)
print('sp_copy =', sp_copy)
print('sp =', sp)

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# print("matrix", matrix)
#
# print("****** FOR IN *******")
# for i, line in enumerate(matrix):
#     for j, el in enumerate(line):
#         print("matrix[{}][{}] = {}".format(i,j,matrix[i][j]))


# Получить имя, если имени нет, то "безымянный"
# people = {"name": "Вася"}
# people = {}
# if people.get("name"):
#     name = people["name"]
# else:
#     name = "Безымянный"
# print(name)
#
# name = people.get("name") or "Безымянный"
#
# print(name)
#
# print(5 or u_var)

#
# d = {"name" : "Vasya"}
#
# print(d.get("name") if d.get("name") else "Безымянный")
#
# # Тернарный оператор конструкция -- истина if условие else Ложь
#
# c = [1,2]
# d = c
# e = [1,2]
# print(c is d)
# print(c is e)

# is оператор является

#
# import random
# # Заполняем список произвольными целыми числами
# lst = []
# for i in range(10):
#      lst.append(random.randint(-10, 10))
#      print('lst = ', lst)
# # С помощью генератора списка
# lst_g = [random.randint(-10, 10) for i in range(10)]
# print('lst_g = ', lst_g)
# # Отбрасываем все отриц. элементы списка
# only_positive = [el for el in lst_g if el >= 0]
# print('only_positive =', only_positive)

# keys = "abcdefg"
# values = range(10)
# dict_g = {key: value for key, value in zip(keys,values)}
# print('dict_g', dict_g)
# dict2_g = {el: el + 4 for el in [1, 4, 6, 8]}
# print('dict2_g', dict2_g)

# a = "Hello \t world"
# print(a)
# b = "Hello \nworld"
# print(b)

# import re
# string = 'This is a simple test message for test'
# string2 = 'test'
# pattern1 = 'test$'
# pattern2 = '^test'
# pattern3 = '^test$'
# print(re.search(pattern1,string)is None)
# print(re.match(pattern2,string)is None)
# print(re.match(pattern3,string)is None)
# print(re.match(pattern3,string2)is None)
#
# import re
# string = 'This is a simple test message for test'
# found = re.findall(r'test',string)
# print(found)

# Найти все цифры в тексте
import re


# pattern = '[0-9]+k'
# string = 'if 300 spartans were so brave, so 500 spartans'\
#     'could destroy more than 10k warriors of Darius, but 15k and even 20k'
# print(re.findall(pattern,string))

# import re
# html = '<p style =''margin-left:10px;>text'
# pattern = '<[^>]+>'
# print(re.findall(pattern,html))
def do_something():
    return "I'm func do_something in module lib1"


def more_then_one(num):
    return num > 1
