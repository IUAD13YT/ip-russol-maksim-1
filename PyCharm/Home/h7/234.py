class Worker:
    def __init__(self, name, surname, salary_rate, staff_position, hours_norm):
        self.name = name
        self.surname = surname
        self.salary_rate = int(salary_rate)
        self.staff_position = staff_position
        self.hours_norm = int(hours_norm)

    def worker_data(self):
        with open('workers', 'r', encoding='UTF-8') as f:
            workers = [Worker]
            for elem in f.readlines()[1:]:
                workers.append(Worker(*elem.split()))

with open('workers', 'r', encoding='UTF-8') as f:
    for line in f:
# class WorkerHours:
#     def __init__(self, name, surname, hours_fact):
#         super().__init__(name, surname)
#         self.hours_fact = hours_fact
# w = Worker
# workers = [Worker() for i in ]


#
# humans = []
# for h in range(7):

# def fill():
# * * f = codecs.open('in.html', 'r', 'utf-8')
# * * for line in f:
# * * * * m = re.findall(u'<a href=\"/org/persons/\d+\">(.*?)</a>', line, flags=re.U|re.DOTALL)
# * * * * for i in m:
# * * * * * * p = Person()
# * * * * * * initials = re.search(u'(\w+)\s(\w+)\s(\w*)', i, flags=re.U)
# * * * * * * if initials != None:
# * * * * * * * * p.surname = initials.group(1)
#     ().append(h)
# objs = [MyClass() for i in range(10)]
# for obj in objs:
#     other_object.add(obj)


# humans = [Human() for elem in range(7)]
# for h in humans:
#     ().append(h)
# # objs = [MyClass() for i in range(10)]
# # for obj in objs:
# #     other_object.add(obj)

# class Try:
#     def do_somthing(self):
#         print('Hello')
#
#
# if __name__ == '__main__':
#     obj_list = []
#     for obj in range(10):
#         obj = Try()
#         obj_list.append(obj)
#
#     obj_list[0].do_somthing()

# def decor(func):
#     def wrap():
#         print('==============')
#         func()
#         print('==============')
#
#     return wrap
#
# @decor
# def print_text():
#     print('Hello World!')
#
#
#
# print_text()
