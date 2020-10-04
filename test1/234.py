class Person:
    def __init__(self, surname, name, f_name):
        self.surname = surname
        self.name = name
        self.f_name = f_name

    def get_full_name(self):
        return f"{self.surname} {self.name} {self.f_name}"

    def full_name_format(self):
        return f"{self.surname} {self.name[0]}. {self.f_name[0]}."

    def male_name_format(self):
        'а'.append(self.surname)
        return f"{self.surname} {self.name[0]}. {self.f_name[0]}."

    def female_name_format(self):
        self.surname = self.surname[:-1] + 'ой'
        return f"{self.surname} {self.name[0]}. {self.f_name[0]}."

    def display_parents_info(self):
        """
        Метод __str__() должен возвращать строку.
        И в данном случае мы возвращаем базовую информацию о человеке.
        И теперь консольный вывод не будет таким: <__main__.Person object at 0x00C0B718>
        """
        print(self.__str__())

    def __str__(self):
        return "{} {} {}".format(self.surname, self.name, self.f_name)


class Student(Person):
    def __init__(self, surname, name, f_name, gender, class_group, father, mother):
        super().__init__(surname, name, f_name)
        self._gender = gender
        self.class_group = class_group
        self.father = father
        self.mother = mother
        self.subjects = {c.subjects_list for c in classes if self.class_group == c.class_name}

    def get_parents(self):
        if self._gender == 'м':
            return print(
                f"Родители ученика \'{self.class_group}\' класса {self.male_name_format()} "
                f"отец: {self.father}, мать: {self.mother}", end='\n')
        else:
            return print(
                f"Родители ученицы \'{self.class_group}\' класса {self.female_name_format()} "
                f"отец: {self.father}, мать: {self.mother}", end='\n')

    # def get_student_subjects(self, class_subjects_list):
    #     return print(
    #         f"Ученик \'{self.class_group}\' класса {self.full_name_format()} "
    #         f"изучает предметы: {self.subjects}", end='\n')
    def get_subjects(self):
        return self.subjects


class Class:
    def __init__(self, class_name, subjects_list):
        self.class_name = class_name
        self.subjects_list = subjects_list
        # self.students_list = {student.full_name_format() for student in students if
        #                       student.class_group in self.class_name}
        # self.teachers_list = {teacher.get_full_name() for teacher in teachers if teacher.subject in self.subjects_list}

    # def class_group_students(self):
    #     return print(f'Ученики \'{self.class_name}\' класса: {self.students_list}', end='\n')
    #
    # def class_group_teachers(self):
    #     return print(f'Учителя, преподающие в \'{self.class_name}\' классе: {self.teachers_list}', end='\n')
    #
    # def class_subjects_list(self):
    #     return print(f'Предметы, которые изучают в \'{self.class_name}\' классе: {self.subjects_list}', end='\n')
class Subject:
    def __init__(self, subject_name, classes_list):
        self.subject_name = subject_name
        self.classes_list = classes_list

dad = [Person('Голубов', 'Геннадий', 'Андреевич'),
       Person('Буданов', 'Степан', 'Адрианович'),
       Person('Мальчиков', 'Руслан', 'Геннадиевич'),
       Person('Попов', 'Модест', 'Прокофиевич'),
       Person('Рагозин', 'Филимон', 'Фролович'),
       Person('Шверник', 'Семен', 'Тимурович'),
       Person('Буров', 'Елисей', 'Сигизмундович'),
       Person('Дуванов', 'Денис', 'Тарасович'),
       Person('Ювелев', 'Емельян', 'Севастьянович'),
       Person('Кручинин', 'Роман', 'Архипович'),
       Person('Задорнов', 'Лавр', 'Фролович'),
       Person('Якунькин', 'Харитон', 'Аникитевич'),
       Person('Евремович', 'Артур', 'Валерьянович'),
       Person('Скоробогатов', 'Зиновий', 'Онисимович'),
       Person('Зарубин', 'Захар', 'Дмитриевич'),
       Person('Паршиков', 'Игорь', 'Федотович'),
       Person('Новосельцев', 'Фока', 'Андреевич'),
       Person('Квартин', 'Феликс', 'Эрнестович'),
       Person('Грибанов', 'Дмитрий', 'Александрович'),
       Person('Николаенко', 'Кузьма', 'Зиновиевич')]
mom = [Person('Голубова', 'Арина', 'Василиевна'),
       Person('Буданова', 'Евгения', 'Игоревна'),
       Person('Мальчикова', 'Виктория', 'Юлиевна'),
       Person('Попова', 'Пелагея', 'Афанасиевна'),
       Person('Рагозина', 'Инга', 'Захаровна'),
       Person('Шверник', 'Любава', 'Филипповна'),
       Person('Бурова', 'Василиса', 'Никитевна'),
       Person('Дуванова', 'Фаина', 'Ипполитовна'),
       Person('Ювелева', 'Рада', 'Святославовна'),
       Person('Кручинина', 'Валерия', 'Георгиевна'),
       Person('Задорнова', 'Пелагея', 'Алексеевна'),
       Person('Якунькина', 'Лариса', 'Алексеевна'),
       Person('Евремович', 'Валентина', 'Серафимовна'),
       Person('Скоробогатова', 'Кристина', 'Тимуровна'),
       Person('Зарубина', 'Нина', 'Фомевна'),
       Person('Паршикова', 'Влада', 'Елизаровна'),
       Person('Новосельцев', 'Розалия', 'Яновна'),
       Person('Квартин', 'Доминика', 'Михеевна'),
       Person('Грибанов', 'Наталья', 'Романовна'),
       Person('Николаенко', 'Анисья', 'Трофимовна')]
classes = [
    Class('6 А', 'Математика, Русский язык, История, Физкультура, Трудовое воспитание'),
    Class('6 Б', 'Математика, Русский язык, История, Физкультура, Трудовое воспитание'),
    Class('7 А', 'История, География, Физкультура, Трудовое воспитание, Математика, Русский язык'),
    Class('7 Б', 'История, География, Физкультура, Трудовое воспитание, Математика, Русский язык'),
    Class('8 А', 'Русский язык, История, География, Физкультура, Экономика, Биология, Физика'),
    Class('8 Б', 'Русский язык, История, География, Физкультура, Экономика, Биология, Физика'),
    Class('9 А', 'География, Химия, Биология, Физика, Экономика, Иностранные языки'),
    Class('9 Б', 'География, Химия, Биология, Физика, Экономика, Иностранные языки'),
    Class('10 А', 'Политология, Информатика, Социология, Химия'),
    Class('10 Б', 'Политология, Информатика, Социология, Химия'),
    Class('11 А', 'Экономика, История, Русский язык, Математика, Иностранные языки, Информатика'),
    Class('11 Б', 'Экономика, История, Русский язык, Математика, Иностранные языки, Информатика'),
]
students = [Student('Голубова', 'Дина', 'Геннадиевна', 'ж', '11 А', dad[0], mom[0]),
            Student('Буданова', 'Агафья', 'Степановна', 'ж', '10 Б', dad[1], mom[1]),
            Student('Мальчиков', 'Лука', 'Руслан', 'м', '9 А', dad[2], mom[2]),
            Student('Попов', 'Фома', 'Модестович', 'м', '8 Б', dad[3], mom[3]),
            Student('Рагозин', 'Герман', 'Филимонович', 'м', '7 А', dad[4], mom[4]),
            Student('Шверник', 'Адам', 'Семенович', 'м', '6 Б', dad[5], mom[5]),
            Student('Буров', 'Никифор', 'Елисеевич', 'м', '5А', dad[6], mom[6]),
            Student('Дуванова', 'Инга', 'Денисовна', 'ж', '11 Б', dad[7], mom[7]),
            Student('Ювелев', 'Мир', 'Емельянович', 'м', '10 А', dad[8], mom[8]),
            Student('Кручинин', 'Иннокентий', 'Романович', 'м', '9 Б', dad[9], mom[9]),
            Student('Задорнов', 'Моисей', 'Лаврович', 'м', '8 А', dad[10], mom[10]),
            Student('Якунькин', 'Наум', 'Харитонович', 'м', '7 Б', dad[11], mom[11]),
            Student('Евремович', 'Фома', 'Артурович', 'м', '6 А', dad[12], mom[12]),
            Student('Скоробогатов', 'Петр', 'Зиновиевич', 'м', '5 Б', dad[13], mom[13]),
            Student('Зарубина', 'Бронислава', 'Захарович', 'ж', '11 А', dad[14], mom[14]),
            Student('Паршиков', 'Платон', 'Игорьевич', 'м', '10 Б', dad[15], mom[15]),
            Student('Новосельцев', 'Пимен', 'Фокаевич', 'м', '9 А', dad[16], mom[16]),
            Student('Квартин', 'Осип', 'Феликсович', 'м', '8 Б', dad[17], mom[17]),
            Student('Грибанов', 'Артемий', 'Дмитриевич', 'м', '7 А', dad[18], mom[18]),
            Student('Николаенко', 'Евдоким', 'Кузьмич', 'м', '6 Б', dad[19], mom[19])]

subjects = [Subject('История', '6 А, 6 Б, 7 А, 7 Б, 8 А, 8 Б, 11 А, 11 Б'),
Subject('Русский язык', '6 А, 6 Б, 7 А, 7 Б, 8 А, 8 Б, 11 А, 11 Б'),
Subject('Математика', '6 А, 6 Б, 7 А, 7 Б, 11 А, 11 Б'),
Subject('Иностранные языки', '9 А, 9 Б, 11 А, 11 Б'),
Subject('Информатика', '10 А, 10 Б, 11 А, 11 Б'),
Subject('Трудовое воспитание', '6 А, 6 Б, 7 А, 7 Б'),
Subject('Физика', '8 А, 8 Б, 9 А, 9 Б'),
Subject('Химия', '9 А, 9 Б, 10 А, 10 Б'),
Subject('Биология', '8 А, 8 Б, 9 А, 9 Б'),
Subject('Физкультура', '6 А, 6 Б, 7 А, 7 Б, 8 А, 8 Б'),
Subject('Социология', '10 А, 10 Б'),
Subject('Экономика', '8 А, 8 Б, 9 А, 9 Б, 11 А, 11 Б'),
Subject('Политология', '10 А, 10 Б'),
Subject('География', '7 А, 7 Б, 8 А, 8 Б, 9 А, 9 Б'),
]

print(students[1].get_subjects())

