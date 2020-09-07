# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random


def mod_square_lst(x):
    new_lst = [el ** 2 for el in x]
    return new_lst


origin_lst = [random.randint(-5, 5) for i in range(7)]
mod_list = mod_square_lst(origin_lst)
print(origin_lst)
print(mod_list,'\n')


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def mod_fruit_lst(l1, l2):
    lst = []
    [lst.append(j) for j in l1 if j in l2]
    return lst


lst_fruits_1 = ['яблоко', 'слива', 'персик', 'виноград', 'апельсин', 'ананас']
lst_fruits_2 = lst_fruits_1.copy()
lst_fruits_2.append('груша')
lst_fruits_2.insert(0, 'банан')
lst_fruits_2.pop(5)
print('Список фруктов №1 =', lst_fruits_1)
print('Список фруктов №2 =', lst_fruits_2)
mod_list = mod_fruit_lst(lst_fruits_1, lst_fruits_2)
print('Срез cписков фруктов №1 и №2 =', mod_list,'\n')

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random


def change_lst(b):
    new_lst = []
    [new_lst.append(j) for j in b if j % 3 == 0 and j > 0 and j % 4 != 0]
    return new_lst


input_list = [random.randint(-10, 50) for h in range(20)]
output_lst = change_lst(input_list)
print(input_list)
print(output_lst)
