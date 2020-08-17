# Методы строк
'''string = 'Hello'
string_test = 'ABCDEFG'
a = 'Start'
b = 'Stop'
c = 'Step'
# string [a:b:c] индексация начинается с 0

# ,title(), .upper(), .lower(), .find(), and etc
print(string_test.find('yy'), len(string_test))
# форматирование строк

name = 'Eric'
surname = 'Smith'
lastname = 'Johnson'
lastname1 = 'Barbaris'
print('Welcome'+name+''+surname+'!')
print('Welcome %s %s !' % (name, surname))
print('Welcome {} {} {}!' .format(name, surname, lastname))
print('Welcome {1} {2} {0} !' .format(name, surname, lastname1))

# списки

empty_list=[]
my_list=[5,4,88,999,9.2,8.75,'abcd','$',777]
print('my_list=', my_list)
print(my_list[3]) #получим 4й эл списка 999
print(my_list[-1]) #получим последний эл списка 777
print(my_list[0:-3]) #получим с 1го по пред-пред последний элемент списка [5, 4, 88, 999, 9.2, 8.75]
print(my_list[0:-3] + [7,8,9]) #получим с 1го по пред-пред последний элемент списка + новый список [5, 4, 88, 999, 9.2, 8.75, 7, 8, 9]

my_list=[1,2,3,4,5,'abcd','$',777]
print('absc' in my_list) #_True
print('abc' in my_list) #_False
my_list = [1,[1,[3]]]
print(my_list)[1][1][0]

# методы списков
lst = [1,2,3]
lst.append(4) #добавить в конец списка
lst.pop() #удалить посл эл
lst.pop(1) #удалить эл с индексом 1
lst

# КОРТЕЖИ
t = (2,)
t = 2,
print(t)

x = [1,2,3]
print(x.pop()) # пустой индекс pop() указывает на последний элемент списка
print(x)
del[0]
print(x)

# Перебор элементов по индексам
fruits = ['apple','orange','banana']
i=0
while len (fruits)>i:
    print('fruit=', fruits[i])
    i +=1


vegetables = ['onion','potato','cucumber']
for vegetavle in vegetables:
    print('vegetavle=', vegetable)

# Словари

# x = {'x','y','z'}
# # {ключ : значение}
# print(x)
# x['y'] = '1'
# print(x)
# x['y']={'1':1}
# print(x)

x = {'y':[],'z':1}
print(x)
x.pop('y')
print(x)
x['y']=1
print(x)'''

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

a = set()
print ('a=',a) #set()
b=set(['a','b','c','c','a','e'])
print('b=',b)
c=set('hello')
print('c=',c)
d={'a','b','c','d'}
print('d=',d)
f={} #А так получится словарь
print('type({})-->', type(f)) #<class 'dict'>
# операции с множествами
ghghng
