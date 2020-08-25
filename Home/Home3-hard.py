# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
e = equation.split(' ')  # print (k) => ['y', '=', '-12x', '+', '11111140.2121']
k = str(e[2])
e[2] = k[:-1]  # print (k, a) => ['y', '=', '-12', '+', '11111140.2121'] -12x
y = float(e[2]) * x + float(e[-1])
print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'
# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

input_date = input('введите дату в формате дд.мм.гггг:')
date = input_date.split('.')
day = int(date[0])
month = int(date[1])
year = int(date[2])
day_31_month = [1,3,5,7,8,10,12]
leap_year = range(1920,3000,4)
if len(date[0]) != 2 or len(date[1]) != 2 or len(date[2]) != 4:
    print('Не корректен формат даты. Следуйте формату дд.мм.гггг')
elif day > 31 or day < 1:
    print('Проверьте корректность ввода значения дня')
elif month == 2 and day > 28:
    print('Проверьте корректность ввода значения дня. Февраль короче')
elif month > 12 or month < 1:
    print('Введён не корректный месяц')
elif year > 3000 or year < 1920:
    print('Введён не корректный год')
elif month not in day_31_month and day > 30:
    print('Проверьте корректность ввода значения дня')
else:
    print('Дата введена корректно: ', input_date)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

n = int(input('ВХОД'
              '\nНОМЕР КОМНАТЫ\n'))
l1 = range(1, 100)
l2 = map(lambda x, y: x * y, l1, l1)
l2 = list(l2)
k = ()
q = 0
while sum(l2[:q]) <= n:
    sum(l2[:q])
    q += 1
k = n - sum(l2[:q - 1])
b = len(l2[:q])  # n-ый блок из n этажей
number = k % b
floor = (sum(l1[0:q - 1]) + int(round((k / b), 0)))
print(f'ВЫХОД'
      f'\nЭТАЖ {floor} ПОРЯДКОВЫЙ НОМЕР НА ЭТАЖЕ {number}')