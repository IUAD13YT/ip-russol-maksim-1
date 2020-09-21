from os import path, chdir, getcwd, mkdir, listdir, rmdir, remove
from shutil import copy
from sys import argv
# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:

if __name__ == '__main__':
    def avg(x, y):
        """Вернуть среднее геометрическое чисел 'a' и 'b'.
        Параметры:
            - x, y (int или float).
        Результат:
            - float.
        """
        return (x * y) ** 0.5


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
    path_dir = getcwd()
    if not (path.exists(path_dir + '/' + dir_name)):
        chdir(path_dir)
        mkdir(dir_name)


def deleting_dirs(dir_name):
    """
    удаление папки из текущей директории
    :param dir_name: название папки
    """
    try:
        dir_path = path.join(getcwd(), dir_name)
        rmdir(dir_path)
    except FileExistsError:
        print(f'Повторное создание уже существующей папки \'{dir_name}\' невозможно')


for i in range(9):
    dir_name = 'dir_' + str(i + 1)
    creating_dirs(dir_name)
    i += 1


print('Папки \'DIR\'s\' созданы!,\n'
      'Cодержимое текущей директории: ')
for cases in listdir(getcwd()):
    print(cases)


for j in range(9):
    dig_name = 'dir_' + str(j + 1)
    deleting_dirs(dig_name)
    j += 1

print('Папки \'DIR\'s\' удалены!,\n'
      'Cодержимое текущей директории: ')
for cases in listdir(getcwd()):
    print(cases)


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


def folder_contents(specified_path):
    """
    выводит содержание папки по заданному пути
    :param specified_path: заданный путь
    """
    for _ in listdir(specified_path):
        print(_)
    return


print(f'Содержимое конечной папки пути \n{getcwd()}')
folder_contents(getcwd())

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copying_file(file):
    """
    копирует содержимое файла file в файл или copy_name
    :param file: исходный файл
    :param copy_name: копия исходника
    :return:
    """

    copy_name = file + '.copy'
    copy(file, copy_name)
    return


# модуль.метод -> shutil.copy(src, dst, follow_symlinks=True) - копирует содержимое файла src в файл или папку dst.


first_file = argv[0]  # h6_0e.py
# а) вызов первого аргумента, argv[0], исполльзует аналогичное скрипту Python наименование.
# б) указываем непосредственное имя файла в текущей директории 'h6_0e.py' или 'test.py'.
copying_file(first_file)
print('Файл, содержащий скрипт скопирован')
question = input('Хотите удалить файл (Да или Нет)?: ')
if question == 'Да':
    path = path.join(getcwd(), argv[0] + '.copy')
    remove(path)
    print('Файл удалён')
