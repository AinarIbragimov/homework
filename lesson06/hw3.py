"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
 income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
 оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
 на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
  и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
  класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': salary, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, salary, bonus):
        super(Position, self).__init__(name, surname, self, salary, bonus)

    def get_total_income(self):
        return f'{self.name}{self.surname}'


if __name__ == '__main__':
    tmp = Position('Анатолий', 'Дукалис', 12000, 1000)
    print(1)
