__author__ = 'Руссол Максим Алнксандрович'

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

age = int(input('(Задача №1)\nВведите ваш возраст (ввод цифрами):\n'))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользоваться данным ресурсом можно только с 18 лет')

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

answer = str(input('(Задача №2)\nВыберите вариант: четные или нечетные?\n'))
if answer == 'четные':
    chetn = list(range(0,22,2))
    print(chetn)
elif answer == 'нечетные':
    nechet = list(range (1,20,2))
    print(nechet)
else:
    while answer != 'четные' or answer != 'нечетные':
        print('Я не понимаю, что вы от меня хотите...')
        answer = str(input('Выберите вариант: четные или нечетные?\n'))

# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.'''

import random
d = int(input('(Задача №3)\nСколько генераций желаете задать (указать числом):\n'))
for a in range (1, d):
       random.seed(a)
       x = random.randint(0, 999999)
       m = max([int(i) for i in str(x)])
       print('Для случайно сгенерированного числа x = ', x, 'максимальное значение цифры в данном числе = ', m)
