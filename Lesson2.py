'''Ветвлениеи циклы'''
'''Логические операции
>  больше
<  меньше
== равно
!= Не равно
>= Больше или равно
<= Меньше или равно'''

# x = 5 > 10
# print (x, type (x))
#True <class 'bool'>

'''# Ctrl+? - quick comment
# ctrl+shift+up/down - перетаскивание строк'''

# /home/dl-academy/Документы/work/ip-russol-maksim-1
'''Инструкции ветвления'''
'''x = 0
print(x)
if x != 1:
    print('Yes')
else:
    print('No')'''
# x = int(input("Enter X = "))
# print(x)
# if x != 1:
#     print('Yes')
# else:
#     print('No')
# '''Enter X = 35
# 35
# Yes'''

# Рассмотрим пример:
# original_password = 'x777'
# password = input('Введите пароль: ')
# access = 0
# if password == original_password:
#     print('Successful Access')
#     access = 1
# if password != original_password:
#     else:
    # print('Access denied')

'''x = 1
print (x)
if x == 1:
    print('Yes')
    x = False
    x = 'False'
    x = ''
    x = 0
    x = []
    x = [1,'']
    x = ['']
if x:
    print('Yyooyoyo')
else: print('No')'''

'''x = 1
print (x)
x = True
if x == 1 or x:
    print('Yes')
elif x == 2:
    print('Noway')
else: print('No')
print(x)'''

# color = 'red'
# if color == 'blue':
#     print ('синий')
# elif color == 'red':
#     print('красный')
# elif color == 'green':
#     print('зелёный')
# else: print('неизвестный цвет')

# !!!Знакомство с циклами!!!'''
# print('Can't do this)
'''  File "/home/dl-academy/Документы/work/ip-russol-maksim-1/Lesson2.py", line 80

IndentationError: unexpected indent'''
# print('Can\'t do this')
# '''Can't do this \' - экранированный символ'''
# a = 0
# while a < 7:
#     print("A")
#     a += 1

'''A
A
A
A
A
A
A'''

# x = input ('Say yes or no: ')
# while x == 'yes':
#     x=input('Say yes or no: ')
# print('YEEEEs')
'''Say yes or no: yes
Say yes or no: e
YEEEEs команда ввода инпут будет повторяться постоянно при вводе yes'''

'''Операторы Break & Continue: !!!!!'''

'''a = 0
while a >= 0:
    if a ==7:
        break
        print ('jgjgjkfd')
    a +=1
    print("jgjgjkfd")

a = -1
while a < 10:
    a += 1
    if a == 7 or a % 2 == 0:
        continue
    print("a --", a)'''

# ЗАЦИКЛИВАНИЕ
a = 5
while a > 0:
    print("!")
    break
    a += 1
#  без брека цикл бесконечен? если нет условия для брейка - то цикл выполниться раз и прервётся

#  ЦИКЛ  FOR \ IN
'''for i in range (5):
    print("Hello")

word_str = 'Hello, World!'
for l in word_str:
    print(l)'''

word_str = 'Hello, World!'
print (word_str[0])
i = 0
for l in word_str:

    if l == 'l':
        i += 1
        if i == 2:
            print(l)
        break
    print(l)

lst = [1,3,5,7,9]