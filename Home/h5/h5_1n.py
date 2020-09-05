# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
'''
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

import re

pattern = '[a-z]+'
str_line_re = re.findall(pattern, line)
print('Нижний регистр строки с модулем (re):\n',
      str_line_re)
print('------------------------------------------------------')


# Функция ord( ) возвращает целое число порядковый номер символа Юникода переданного в качестве аргумента.

# Функция chr( ) возвращает строку (str) с символом Юникода номер которого равен значению аргумента.
def symbols_unicode_AZ(a, z):
    A = ord('A')
    Z = ord('Z')
    symbols_list = []
    for letter in range(A, Z + 1):  # 65(A) - (90)Z +1 особенность range
        symbols_list.append(chr(letter))
    return symbols_list


symbol_list = symbols_unicode_AZ(65, 90)

line = list(line)

for i, el in enumerate(line):
    for letter in symbol_list:
        if el == letter:
            line[i] = ' '
str_line_nore = ''.join(line).split(' ')  # Метод split('separator') разбивает строку на части, используя
                                          # специальный разделитель(separator) ' '(у нас отступ),
                                          # и возвращает эти части в виде списка.

                                          # Методом, выполняющим обратные действия методу .split()
                                          # является метод списков .join(), который собирает строку из элементов списка.
                                          # Метод separator.join(list) - cобирает из списка list строку с разделителем элементов separator

str_line_nore = [i for i in str_line_nore if i != ''] #удаление всех пустых строковых значений скиска
print('Символы нижнего регистра без модуля (re):\n', str_line_nore)
print('------------------------------------------------------')
'''

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
'''
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm' \
         'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV' \
         'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA' \
         'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV' \
         'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW' \
         'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC' \
         'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR' \
         'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm' \
         'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn' \
         'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS' \
         'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf' \
         'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH' \
         'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN' \
         'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ' \
         'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
import re
pattern = '[a-z]{2}([A-Z]*)[A-Z]{2}' # условие регулярного выражения
list_line_task_2 = re.findall(pattern, line_2)
list_line_task_2 = [i for i in list_line_task_2 if i != ''] # удаление всех пустых строковых значений скиска
print('Список c использованием модуля re: \n',list_line_task_2)


A_Z = list(map(lambda x: chr(x), list(range(65, 91))))  # генерируем алфавит ABC верхнего регистра
a_z = list(map(lambda x: chr(x), list(range(97, 123)))) # генерируем алфавит abc
line_2 = list(line_2)
print((len(line_2)))
lst = []
i = len(line_2) - 1 # задаем i - счетчик цикла длиною на 1 эл. < списка условия задачи
# Находим  символ в верхнем регистре после которого стоят еще два символа в верхнем регистре
while i >= 0:
       if line_2[i] in a_z:
              lst.append(line_2[i])
       elif line_2[i] in A_Z and i <= len(line_2) - 3 and line_2[i + 1] in A_Z and line_2[i + 2] in A_Z:
              lst.append(line_2[i])
       else:
              lst.append(' ')
       i -= 1
# результат действий цикла с использованием метода .append() реверсировал выборку относительно исходного списка
lst.reverse()  # Переворачиваем список

i = 0
lst2 = []
# Фильтрация списка.
while i <= len(lst) - 1:
       if lst[i] in A_Z and lst[i - 1] in a_z and lst[i - 2] in a_z:
              lst2.append(lst[i])
       elif lst[i] in A_Z:
              lst2.append(lst[i])
       else:
              lst2.append(' ')
       i += 1
list_line_task_2_nore = ''.join(lst2).split(' ')  # Преобразование в строку и разбиение по пробелам
list_line_task_2_nore = [i for i in list_line_task_2_nore if i != '']  # Формирование выходного списка из строки
print('Список без использованием модуля re: \n', list_line_task_2_nore)
print('------------------------------------------------------') '''

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

from random import randint

x = input('введите имя файла, например h5_1n:\n') + '.txt'
f5 = open(x, 'w+')
digits = [randint(0, 9) for i in range(2500)]

for i in digits:
    print(i, end='', file=f5)
print(file=f5)

f5.close()

f5 = open(x, 'r')
digits2500list = f5.read()
print('Проверяем созданный файл! В Терминале информация дублируется для лишь удобства (противоречит услвию)!')
print('Сгенерированное 2500-значное произвольное число:')
print(digits2500list)
f5.close()


def long_combo(x, y):
    from re import findall as poisk
    z = poisk(x, y)
    return z


pattern_1 = '([0]{3,9}|[1]{3,9}|[2]{3,9}|[3]{3,9}|[4]{3,9}|[5]{3,9}|[6]{3,9}|[7]{3,9}|[8]{3,9}|[9]{3,9})'
res_1 = long_combo(pattern_1, digits2500list)

m = max(map(len, res_1))
print('Максимальная последовательность одинаковых рядомстоящих цифр равна m =', m)
print(f'Вывод последовательности(ей) размерностью {m}:')
f5 = open(x, 'a+')
for i in res_1:
    if len(i) == m:
        print(i, end=' ', file=f5)
f5.close()