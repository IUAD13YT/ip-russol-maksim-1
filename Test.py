import random
a = 0
while a < 10:
    a += 1
    random.seed(a)
    x = str(random.randint(0, 99999))
    m = max(i for i in x)
    print('Cлучайное число x = ', x, 'максимальное значение цифры в данном числе = ', m)
