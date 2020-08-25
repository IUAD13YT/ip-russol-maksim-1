import math

'''n = 60
list1 = range(1,100)
l2 = map(lambda x, y: x * y, list1, list1)
l2 = list (l2)
k = ()
for q in range(len(l2)-1):
    q=0
    sum(l2[:q]) < n < sum(l2[:q+1])
    q +=q
    k = n - sum(l2[:q])

print (k)
print (sum(l2[:q]))'''
import math

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

#     print(max(sum(l2[0:i])))
# for i,y in enumerate(l2): #- Возвращает пары,(элемент, его индекс) только для последовательностей
#      print(i+1,y)
# print (math.sqrt(9216))
# a = range (1,96)
# def listsum(numList):
#    if len(numList) == 1:
#         return numList[0]
#    else:
#         return numList[0] + listsum(numList[1:])

#    for i in (len(l2 - 1)):
#        max(int(sum(l2[0:i]))) <= n
#        print(max(sum(l2[0:i])))
#    for i, y in enumerate(l2):  # - Возвращает пары,(элемент, его индекс) только для последовательностей
#        print(i + 1, y)
#    print(math.sqrt(9216))
#    a = range(1, 96)
#
#    def listsum(numList):
#        if len(numList) == 1:
#            return numList[0]
#        else:
#            return numList[0] + listsum(numList[1:])
#
# print(listsum(range(1,96)))
#
# c = range(56,91,1)
# d = list(c)
# print(d)
# for i,y in enumerate(d): #- Возвращает пары,(элемент, его индекс) только для последовательностей
#      print(i+1,y)
#
# print((16/6)+(1+2+3+4+5))
