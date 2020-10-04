# ООП
# class - шаблон для создания объектов
# Классы содержат атрибуты - данные, и методы - функции для обработки данных
# class Student:
#     # функция - конструктор - запускается автоматически при создании объекта
#     # (экземпляр класса)
#     def __init__(self, name, surname, age, school, class_room):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.school = school
#         self.class_room = class_room
#
#     def next_class(self):
#         self.class_room = str(int(self.class_room.split()[0]) + 1) + ' ' + \
#                           self.class_room.split()[1]
#
#     # метод
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def set_name(self, new_name):
#         self.name = new_name


# student1 = Student("Александр", "Иванов", "10.11.1998", "8 гимназия", "5 А")
# student2 = Student("Петр", "Сидоров", "10.01.1995", "8 гимназия", "8 Б")
# student1.name = 'Guliam'
# print(student1.class_room)
# student1.next_class()
# print(student1.class_room)

# #
# # class Teacher:
# #     def __init__(self, name, surname, age, school, class_list):
# #         self.name = name
# #         self.surname = surname
# #         self.age = age
# #         self.school = school
# #         self.class_list = class_list
# #
# #         # метод
# #
# #     def get_full_name(self):
# #         return self.name + ' ' + self.surname
# #
# #     def set_name(self, new_name):
# #         self.name = new_name
# #
#
class Person:
    def __init__(self, name, surname, age, school):
        self.name = name
        self.surname = surname
        self.age = age
        self.school = school

    def full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name
#
#
# class Student(Person):
#     def __init__(self, name, surname, age, school, class_room):
#         Person.__init__(self, name, surname, age, school)
#         self._class_room = class_room
#
#     def set_new_class_room(self, class_room):
#         self._class_room = class_room
#
#     # @property - позволяет обращаться к методу как  к атрибуту
#     # .class_room() --> .class_room
#     @property
#     def get_class_room(self):
#         return self._class_room
#
#
class Teacher(Person):
    room = 'default'

    def __init__(self, name='Gordey', surname='Manukian', age='31', school='43', class_list='4b,3c,5d'):
        Person.__init__(self, name=name, surname=surname, age=age, school=school)
        self._class_list = class_list
        # self.room = '12456'

    def set_new_class_list(self, class_list):
        self._class_list = class_list

    def get_class_list(self):
        return self._class_list
#
#
# # student_1 = Student("Maks", "Russol", "22", "school", "2d")
teacher_1 = Teacher("Svetlana", "Gotsiuk", "39", "school", ' ')
teacher_2 = Teacher()
# print(teacher_2.full_name())
# # print(student_1.full_name())
# # print(student_1.get_class_room)
# # student_1.set_new_class_room('2a')
#
# # print(student_1.get_class_room())
#
print(teacher_1.full_name())
print(teacher_1.get_class_list())
print(teacher_1.room)
# # teacher_1.set_new_class_list('2a')
# # print(teacher_1.get_class_list())
# print(teacher_1.room)
