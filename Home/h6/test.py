import os
import shutil
import sys
def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)


first_file = sys.argv[0]
backup_file = first_file + '.copy'
copy_file(first_file,backup_file)


def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - такой директории нет')


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')

# dir_path = 'C:\\Users\\rvsiv\\Documents\\Учеба\\Питон\\Python 1\\Lesson5\\dir_9'
# change_dir(dir_path)