# Задача:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
from easy import creating_dirs, deleting_dirs, folder_contents, copying_file

path = 'C:/Users/user/PycharmProjects/ip-russol-maksim-1/'
os.getcwd()
print(os.getcwd())


def folders_menu():
    while True:
        print("""
                                        Меню выбора действия
                                Выберите пункт для необходимого действия:
1. Перейти в папку                           3. Удалить папку               0. Выход из меню
2. Просмотреть содержимое текущей папки      4. Создать папку""")

        action = input()
        try:
            if action == '1':
                dir_name = input('Название папки dir_name: ')
                if dir_name in folder_contents():
                    os.chdir(dir_name)
                    print('Успешно выполнен переход в папку %s' % dir_name)
                    print(os.getcwd())
                else:
                    print('Невозможно перейти в папку %s. Папки не существует' % dir_name)
            elif action == '2':
                for i in folder_contents():
                    print(i)
            elif action == '3':
                dir_name = input('Название папки dir_name: ')
                if dir_name in folder_contents():
                    deleting_dirs(dir_name)
                    print('Успешно удалена папка %s' % dir_name)
                    print(folder_contents())
                else:
                    print('Невозможно удалить несуществующую папку %s' % dir_name)
            elif action == '4':
                path_dir = os.getcwd()
                dir_name = input('Название папки dir_name: ')
                from os import path, chdir, getcwd, mkdir
                if not (path.exists(path_dir + '/' + dir_name)):
                    chdir(path_dir)
                    mkdir(dir_name)
                    print('Успешно создана папка %s' % dir_name)
                    print(folder_contents())
                    continue
                else:
                    print('Невозможно создание папки \'%s\'! Папка уже существует.' % dir_name)
            elif action == '0' or action == 'q':
                print("Выход из меню выбора действия")
                break
        except ValueError:
            print("выберите что-то из нужного")


folders_menu()
