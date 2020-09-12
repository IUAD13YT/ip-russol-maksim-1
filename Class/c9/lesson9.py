# foo = long_function_name()

# with open('/path/gbhjkjhgcvbnm,mnbvbnklkjnbv') as file_1, \
#      open('/dfklgkldfngdfngdfmdf;gm;dfmg;dfmg;mdf;g') as file_2:
#     file_2.write(file_1.read())

# import os - стандартные либы
# import - сторонняя либа
# import builder - ваши модули

# пробелы:

# spam(Ham[1], {eggs:2}) # - правильно
# spam( Ham[ 1 ], { eggs: 2 }) # - неправильно

# if x == 4: print(x, y); x, y = y, x - правильно
# if x == 4 : print(x , y) ; x , y = y , x - неправильно

# spam(1) + / spam (1) !!!

# JSON - текстовый формат обмена данными, основанный на JavaCcript

'''import json
data = {'name': 'Максим',
        'surename': 'Руссол',
        'address': {'city': 'HOLLYWOOD', 'street': 'Ushakova'}
        }
with open ('l9_file.json', 'w') as outfile:
    json.dump(data, outfile)     # json.dump - запись

with open('l9_file.json', 'r') as f:
    data2 = json.loads(f.read())  # json.loads - выгрузить, считать .json к виду .py
    print(data2) '''

'''
class WorkerBuilder:
    def __init__(self, d):
        for key, value in d.items():
            setattr(self, key, value) # setattr - присваивает к текущей функции/ объекту- значение


worker = WorkerBuilder({'name': 'Максим', 'surename': 'Руссол'})
worker_2 = WorkerBuilder({'name': 'Александр', 'surename': 'Маслов', 'age': '40'})
print(worker.name)
print(worker.surename)
print(worker_2.age)


# def __init__(self, name='Gordey', surname='Manukian', age='31', school='43', class_list='4b,3c,5d'):
#     Person.__init__(self, name=name, surname=surname, age=age, school=school)
#     self._class_list = class_list
#     # self.room = '12456'

class HousingBuilder:

    def __init__(self,data,):
        for key, value in data.items():
            setattr((self), key, value)

class HouseHolder(WorkerBuilder):
    def __init__(self, d):
        for key, value in d.items():
            setattr(self, key, value) # setattr - присваивает к текущей функции/ объекту- значение

householder_1 = WorkerBuilder({'name': 'Максим', 'surename': 'Руссол'})
house_holder_2 = WorkerBuilder({'name': 'Александр', 'surename': 'Маслов', 'age': '40'})

house_1 = HousingBuilder({'type': 'Квартира',
        'Square': '220',
        'rooms': '4',
        'address':
            {'city': 'HOLLYWOOD',
             'street': 'Ushakova',
             'postCode': '445028'}
        })
house_2 = HousingBuilder({'type': 'Дом',
        'Square': '550',
        'pool': 'YES',
        'address':
            {'city': 'Херсон',
             'street': 'Ленина',
             'postCode': '73003'}
        })
print(house_2.Square)
print(house_1.rooms)
print(house_1.address)
print(house_2.pool)
print(householder_1.name)

# для патерна - билдер библиотека
'''


# наследование - предача всех методов
# Агрегирование или делегирование - определенные методы


class A:

    def f(self):
        print("A: vyzyvaem metod F")

    def g(self):
        print("A: vyzyvaem metod G")


class C:

    def __init__(self):
        self.A = A()

    def f(self):
        return self.A.f()

    def g(self):
        return self.A.g()


c = C()
c.f()  # "A: vyzyvaem metod F"
c.g()  # "A: vyzyvaem metod G"
