# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
import os

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


def creating_dirs(dir_name):
    """
    создание папки в текущей директории
    :param dir_name: название папки
    :return:
    """
    import os
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.mkdir(dir_path)


def deleting_dirs(dir_name):
    """
    удаление папки из текущей директории
    :param dir_name: название папки
    :return:
    """
    import os
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.rmdir(dir_path)


for i in range(9):
    try:
        dir_name = 'dir_' + str(i + 1)
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.rmdir(dir_path)
        i += 1
    except FileNotFoundError:
        print('Невозможно удалить несуществующие папки')
        question = input('Хотите создать папки (Да или Нет)?:')
        if question == 'Да':

try:
    for i in range(9):
        name = 'dir_' + str(i + 1)
        creating_dirs(name)
        i += 1
except FileExistsError:
    print('Папки уже созданы')

    question = input('Хотите удалить папки (Да или Нет)?:')
    if question == 'Да':
        for i in range(9):
            deleting_dirs(name)

 try:
        dir_name = 'dir_' + str(i + 1)
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.rmdir(dir_path)
        i += 1
    except FileNotFoundError:
        print('Невозможно удалить несуществующие папки')


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


def folder_contents(specified_path):
    """
    выводит содержание папки по заданному пути
    :param specified_path: заданный путь
    :return:
    """
    import os
    for cases in os.listdir(specified_path):
        print(cases)
    return


print(f'Содержимое конечной папки пути \n{os.getcwd()}')
folder_contents(os.getcwd())


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

filter()
def copying_file(file):
    """
    копирует содержимое файла file в файл или copy_name
    :param file: исходный файл
    :param copy_name: копия исходника
    :return:
    """
    import shutil
    copy_name = file + '.copy'
    shutil.copy(file, copy_name)
    return

# shutil.copy(src, dst, follow_symlinks=True) - копирует содержимое файла src в файл или папку dst.
import sys
first_file = sys.argv[0]  # h6_0e.py
# а) вызов первого аргумента, argv[0], исполльзует аналогичное скрипту Python наименование.
# б) указываем непосредственное имя файла в текущей директории 'h6_0e.py' или 'test.py'.
copying_file(first_file)
print('Файл, содержащий скрипт скопирован')
question = input('Хотите удалить файл (Да или Нет)?: ')
if question == 'Да':
    path = os.path.join(os.getcwd(), sys.argv[0] + '.copy')
    os.remove(path)
    print('Файл удалён')
