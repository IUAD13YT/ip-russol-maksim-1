# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Worker:
    def __init__(self, name, surname, salary, position, norm_hours):
        self.name = name
        self.surname = surname
        self._salary = int(salary)
        self.position = position
        self.norm_hours = int(norm_hours)
        self.work_hours = 0

    def read_work_hours(self):
        with open('hours_of', 'r', encoding='UTF-8') as f:
            for line in f():
                if line.split()[0] == self.name and i.split()[1] == self.surname:
                    self.work_hours = int(i.split()[2])
                    break
                else:
                    continue

    def calc_salary(self):
        for_hour = self._salary // self.norm_hours
        salary = 0
        if self.work_hours > self.norm_hours:
            razn = self.work_hours - self.norm_hours
            salary = (razn * for_hour) * 2
            return (salary + self._salary)
        elif self.work_hours < self.norm_hours:
            razn = self.norm_hours - self.work_hours
            salary = razn * for_hour
            return (self._salary - salary)
        else:
            return (self._salary)

    def write_salary(self, salary):
        with open('salary_for_all.txt', 'a', encoding='UTF-8') as f:
            f.write(self.name + ' ' + self.surname + ' ' + str(salary) + ' ' + self.position)
            f.write('\n')


def file_handle(file):
    f = open(file, 'r', encoding='UTF-8')
    for i in f.readlines():
        if i.count('Имя') == 1:
            continue
        else:
            # обработка строки
            name, surname, salary, position, norm_hours = i.split()
            workman = Worker(name, surname, salary, position, norm_hours)
            workman.read_work_hours()
            salary = workman.calc_salary()
            workman.write_salary(salary)
    f.close()


file_handle('workers')