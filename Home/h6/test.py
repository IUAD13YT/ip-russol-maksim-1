import os
import shutil
import sys


# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


'''

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


def folders_in_directory(the_path):
    for cases in os.listdir(the_path):
        print(cases)
    return cases


print(f'Содержимое конечной папки пути \n{os.getcwd()}')
folders_in_directory(os.getcwd())


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file(src, dst):
    shutil.copy(src, dst)
    return shutil.copy


# shutil.copy(src, dst, follow_symlinks=True) - копирует содержимое файла src в файл или папку dst.

first_file = sys.argv[0]  # h6_0e.py
# а) вызов первого аргумента, argv[0], исполльзует аналогичное скрипту Python наименование.
# б) указываем непосредственное имя файла в текущей директории 'h6_0e.py' или 'test.py'.
backup_file = first_file + '.copy'
copy_file(first_file, backup_file)
print('Файл, содержащий скрипт скопирован')
if os.access((sys.argv[0] + '.copy'), os.F_OK):
    path = os.path.join(os.getcwd(), sys.argv[0] + '.copy')
    os.remove(path)

'''
