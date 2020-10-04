class Person:
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name


class Pupil(Person):
    def __init__(self, class_room, surname, name):
        super().__init__(surname, name)
        self.class_room = class_room

    def full_name(self):
        self.surname, '', self.name


class Class:
    def __init__(self, class_list):
        self.class_list = {c.class_room for c in pupils}



pupils = [Pupil('Голубова', 'Дина', '11'),
          Pupil('Буданова', 'Агафья', '11'),
          Pupil('Мальчиков', 'Лука', '11'),
          Pupil('Попов', 'Фома', '11'),
          Pupil('Рагозин', 'Герман', '10'),
          Pupil('Шверник', 'Адам', '9'),
          Pupil('Буров', 'Никифор', '9'),
          Pupil('Дуванова', 'Инга', '8'),
          Pupil('Ювелев', 'Мир', '10'),
          Pupil('Кручинин', 'Иннокентий', '9')]