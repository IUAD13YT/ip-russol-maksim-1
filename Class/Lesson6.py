# # Существует три типа ошибок, которые могут возникнуть в программах:
# # Синтаксические ошибки (syntax errors);
# # Ошибки выполнения(runtime errors);
# # Семантические ошибки(semantic errors).
# f = open('1.txt')
# ints = []
# try:
#     for line in f:
#         ints.append(int(line))
# except ValueError:
#     print('Это не число. Выходим.')
# except Exception:
#     print('Это что еще такое?')
# else:
#     print('Всё хорошо')
# finally:
#     f.close()
#     print('Я закрыл файл.')
# # именно в таком порядке: try, группа except, затем else, и только потом finally.
#
# # print("start")
# # try:
# #     val = int(input("input number: "))
# #     tmp = 10 / val
# # except(ValueError,ZeroDivisionError):
# #     print("Error!")
# # print("Stop")
#
# # print("start")
# # try:
# #     val = int(input("input number: "))
# #     tmp = 10 / val
# #     print(tmp)
# # except ValueError as ve:
# #     print("VallueError! {0}".format(ve))
# # except ZeroDivisionError as zde:
# #     print("ZeroDivisionError! {0}".format(zde))
# # except Exception as ex:
# #     print("Error! {0}".format(ex))
# # print("Stop")
#
# try:
#     raise Exception("Some exception")  # Для принудительной генерации исключения используется инструкция raise.
# except Exception as e:
#     print("Exception exception " + str(e))
# # МОДУЛИ
# # Каждый файл — это отдельный модуль, модули могут импортировать другие модули для доступа к именам, которые в них определены.
# #
# # Обработка модулей выполняется двумя инструкциями и одной важной функцией:
# # Позволяет клиентам (импортерам) получать модуль целиком — import.
# # Позволяет клиентам получать определённые имена из модуля — from.
# # Обеспечивает возможность повторной загрузки модуля без остановки интерпретатора — imp.reload.
# # UPD.Начиная с версии Python3.4, imp.reload() запрещён. Вместо этого — importlib.reload().
# a = 10
# from math import sin as x, sqrt as y
# print (x(0.2))
# print (int(y(4)))

# import new as my_lib
# print(my_lib.do_something())
#
# import lesson5 as my_lib
# print(my_lib.more_then_one(2))

# import os
# print('os.name = ', os.name)
# print('os.getcwd() = ', os.getcwd())
#
# dir_path = os.path.join(os.getcwd(), 'NewDir')
# try:
#     os.mkdir(dir_path)
# except FileExistsError:
#     print('Такая директория уже существует')
#     os.rmdir(dir_path)
#     print('Директория удалена')
# Модуль SYS

'''import sys
print('sys.argv = ', sys.argv) # полный путь к файлу скрипта
print('sys.path = ', sys.path) #список путей для поиска модулей
print('sys.executable = ', sys.executable) #полный путь к интерпретатору
print('sys.modules = ', sys.modules) #словарь загруженных модулей
print('sys.platform = ', sys.platform) #информация об ОС
while True:
    key = input("press 'q' to Exit")
    if key == 'q':
        sys.exit()'''
# import sys
# import argparse
#
#
# def createParser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('name', nargs='?', default='мир')
#     return parser
#
#
# if __name__ == '__main__':
#     parser = createParser()
#     namespace = parser.parse_args(sys.argv[1:])
#
#     print('Привет {}!'.format(namespace.name))

# УСТАНОВКА ПАКЕТОВ С ПОМОЩЬЮ PIP
# pip - это система управления пакетами, которая используется для установки и управления программными пакетами, написанными на Python.

# easy_install <>
# pypi.com
# sudo apt-get install python3-venv /# pip3 install virtualenv
# python3 -m venv env