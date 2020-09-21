# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
# class Triangle ():

import math


def input_dots(dot):
    """
    Функция задает вводимые пользователем координаты точек
    :param dot: количество точек с парой координай (x, y)
    :return: возвразает многомерный список,
    каждый эелемент которого это одна точка с координатами в виде списка
    """
    s = []
    print('Введите попарно координаты каждой точки через пробел')
    for i in range(dot):
        row = input(f'Координаты {i + 1}-й точки: ').split()
        for elem in range(len(row)):
            row[elem] = int(row[elem])
        s.append(row)
    return s


def print_three(three):
    print('Периметр треугольника: ', three.perimeter_of_triangle())
    print('Площадь треугольника: ', three.square_of_triangle())
    print('Высота треугольника: ', three.height_of_triangle())
    print()
    return ()


class Triangle:
    def __init__(self, q, w, e):
        def side_of_triangle(t1, t2):
            return math.sqrt(((t2[0] - t1[0]) ** 2) +
                             ((t2[1] - t1[1]) ** 2))

        self.A = q
        self.B = w
        self.C = e

        self.a = side_of_triangle(self.A, self.B)
        self.b = side_of_triangle(self.B, self.C)
        self.c = side_of_triangle(self.A, self.C)

    def perimeter_of_triangle(self):
        return round((self.a + self.b + self.c), 2)

    def square_of_triangle(self):
        half_perimeter = self.perimeter_of_triangle() / 2
        return round((math.sqrt(half_perimeter *
                                (half_perimeter - self.a) *
                                (half_perimeter - self.b) *
                                (half_perimeter - self.c))), 2)

    def height_of_triangle(self):
        return round((self.square_of_triangle() / (self.a / 2)), 2)


dots_1 = input_dots(3)
prim_three = Triangle(dots_1[0], dots_1[1], dots_1[2])
print_three(prim_three)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


def print_trap(trap):
    print(trap.trap_checking())
    print('Cтороны трапеции', trap.sides())
    print('Периметр трапеции', trap.perimeter_of_trap())
    print('Высота трапеции', trap.height_of_trap())
    print('Площадь трапеции', trap.square_of_trap())
    return ()


try:

    class trapeze:
        def __init__(self, q, w, e, r):
            def sides_and_diagonals_of_trap(t1, t2):
                return ((t2[0] - t1[0]) ** 2 +
                        (t2[1] - t1[1]) ** 2)

            def parallels(a, b, c, d):
                ad = [j - k for j, k in zip(d, a)]
                nad = math.sqrt(sum([i ** 2 for i in ad]))
                adn = [i / nad for i in ad]
                bc = [j - k for j, k in zip(c, b)]
                nbc = math.sqrt(sum([i ** 2 for i in bc]))
                bcn = [i / nbc for i in bc]
                dif_1 = (sum([j - k for j, k in zip(adn, bcn)]))
                ab = [j - k for j, k in zip(b, a)]
                nab = math.sqrt(sum([i ** 2 for i in ab]))
                abn = [i / nab for i in ab]
                dc = [j - k for j, k in zip(c, d)]
                ndc = math.sqrt(sum([i ** 2 for i in dc]))
                dcn = [i / ndc for i in dc]
                dif_2 = (sum([j - k for j, k in zip(abn, dcn)]))
                if dif_1 == 0:
                    return 1
                elif dif_2 == 0:
                    return 2
                else:
                    return 3

            self.A = q
            self.B = w
            self.C = e
            self.D = r

            self.sideAB = round((sides_and_diagonals_of_trap(self.A, self.B)), 2)
            self.sideBC = round((sides_and_diagonals_of_trap(self.B, self.C)), 2)
            self.sideCD = round((sides_and_diagonals_of_trap(self.C, self.D)), 2)
            self.sideAD = round((sides_and_diagonals_of_trap(self.A, self.D)), 2)
            self.dig_1 = round((sides_and_diagonals_of_trap(self.A, self.C)), 2)
            self.dig_2 = round((sides_and_diagonals_of_trap(self.B, self.D)), 2)

            self.parallels = parallels(self.A, self.B, self.C, self.D)
            self.answer = 'Фигура не определена как трапеция по основным её свойствам'
            self.answer_AD_BC = 'успешная проверка: фигура - равнобедренная трапеция. AD и BC - паралельные основания'
            self.answer_AB_DC = 'успешная проверка: фигура - равнобедренная трапеция. AB и DC - паралельные основания'

        def trap_checking(self):
            if self.dig_1 == self.dig_2:
                if self.parallels == 1:
                    return self.answer_AD_BC
                else:
                    return self.answer_AB_DC
            elif self.sideAB == self.sideCD and self.parallels == 1:
                return self.answer_AD_BC
            elif self.sideAD == self.sideBC and self.parallels == 2:
                return self.answer_AB_DC
            else:
                raise SystemExit(print(self.answer))

        def sides(self):
            return self.sideAB, self.sideBC, self.sideAD, self.sideCD

        def perimeter_of_trap(self):
            return self.sideAB + self.sideAD + self.sideBC + self.sideCD

        def height_of_trap(self):
            if self.trap_checking() == self.answer_AD_BC:
                return round(math.sqrt((self.sideBC ** 2) -
                                       (((self.sideAD - self.sideAB) ** 2) + (self.sideBC ** 2) - (self.sideCD ** 2)) /
                                       (self.sideAD - self.sideAB) * 2), 2)
            elif self.trap_checking() == self.answer_AB_DC:
                return round(math.sqrt((self.sideCD ** 2) -
                                       (((self.sideAB - self.sideBC) ** 2) + (self.sideCD ** 2) - (self.sideAD ** 2)) /
                                       (self.sideAB - self.sideBC) * 2), 2)

        def square_of_trap(self):
            if self.trap_checking() == self.answer_AD_BC:
                return round((((self.sideAD + self.sideBC) * self.height_of_trap()) / 2), 2)
            elif self.trap_checking() == self.answer_AB_DC:
                return round((((self.sideAB + self.sideCD) * self.height_of_trap()) / 2), 2)


    td = input_dots(4)
    prim_trap = trapeze(td[0], td[1], td[2], td[3])
    print_trap(prim_trap)

except ZeroDivisionError:
    print('Координаты точек не подходят в качестве вершин четырехугольника')
