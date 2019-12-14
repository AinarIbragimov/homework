"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    __asphalt_mass = 25

    def __init__(self, lenght, width):
        """
        :param lenght: digit: road lenght in meters
        :param width: digit: road width in meters
        """
        self._length = float(lenght)
        self._width = float(width)

    def asphalt_sum(self, thickness=1):
        return self._length * self._width * self.__asphalt_mass * thickness
