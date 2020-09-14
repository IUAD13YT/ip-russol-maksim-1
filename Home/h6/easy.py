def creating_dirs(path_dir, dir_name):
    """
    создание папки в текущей директории
    :param path_dir:
    :param dir_name: название папки
    :return:
    """
    from os import path, chdir, getcwd, mkdir
    if not (path.exists(path_dir + '/' + dir_name)):
        chdir(path_dir)
        mkdir(dir_name)
    else:
        print('Невозможно создание папки \'%s\'! Папка уже существует.' % dir_name)


def deleting_dirs(dir_name):
    """
    удаление папки из текущей директории
    :param dir_name: название папки
    :return:
    """
    from os import path, getcwd, rmdir
    try:
        dir_path = path.join(getcwd(), dir_name)
        rmdir(dir_path)
    except FileExistsError:
        print(f'Повторное создание уже существующей папки \'{dir_name}\' невозможно')


def folder_contents():
    """
    выводит содержание папки по заданному пути
    :param specified_path: заданный путь
    :return:
    """
    from os import listdir, getcwd
    # for cases in listdir(getcwd()):
    #     print(cases)
    return listdir(getcwd())


def copying_file(file):
    """
    копирует содержимое файла file в файл или copy_name
    :param file: исходный файл
    :param copy_name: копия исходника
    :return:
    """
    from shutil import copy
    copy_name = file + '.copy'
    copy(file, copy_name)
    return

# path_dir = 'C:/Users/user/PycharmProjects/ip-russol-maksim-1/Home/h6'
# path_dir = os.getcwd()
