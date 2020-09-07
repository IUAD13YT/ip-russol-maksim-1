# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
from os import listdir


def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.
    Параметры:
        - a, b (int или float).
    Результат:
        - float.
    """
    return (a * b) ** 0.5


while True:
    try:

        a = float(input("a = "))
        b = float(input("b = "))
        c = float(avg(a, b))
        # print("Среднее геометрическое = {:.2f}".format(c))
        print(c)

    except ValueError as err:
        print("Ошибочка:', err, 'Это не число! Введите число цифрами:")
    except TypeError as typeerr:
        print(f"Блииин ошибка:{typeerr} Невозможно определить среднее геометрическое"
              "\nвведенных чисел (а и b) - подкорневые множители."
              "\n(a и b ='-') / (a и b = '+') !")
    except Exception as ex:
        print("Ошибка:", ex)
    else:
        break

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

try:
    for i in range(9):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i + 1))
        os.mkdir(dir_path)
        i += 1
except FileExistsError:
    print('Папки уже созданы')


    def delete_dirs(the_path):
        for i in range(9):
            our_path = os.path.join(the_path, 'dir_' + str(i + 1))
            os.rmdir(our_path)

        return i


    question = input('Хотите удалить папки (Да или Нет)?:')
    if question == 'Да':
        delete_dirs(os.getcwd())

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


import os


def folders_in_directory(the_path):
    for cases in os.listdir(the_path):
        print(cases)
    return cases


print(f'Содержимое кончной папки пути \n{os.getcwd()}')
folders_in_directory(os.getcwd())

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil
import sys
def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)
    return shutil.copy

first_file = sys.argv[0]
backup_file = first_file + '.copy'
copy_file(first_file,backup_file)