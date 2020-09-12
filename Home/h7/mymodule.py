def add(a, b):
   return a + b

def sub(a, b):
   return a - b

def mul(a, b):
   return a * b

def div(a, b):
   return a / b
bdadgdg
ssfsdfdgf
dfhdhdghdgfh
def deleting_dirs(dir_name):
    import os
    """
    удаление папки из текущей директории
    :param dir_name: название папки
    :return:
    """
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.rmdir(dir_path)

    from random import randint