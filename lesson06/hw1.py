"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
import time
from itertools import cycle
from time import sleep
from tkinter import *


class TrafficLight:
    __modes = (('red', 7), ('yellow', 2), ('green', 5), ('yellow', 2))
    __light_start = 0
    __next_light = 0

    def __init__(self):
        self.__color = self.__modes[0][0]

    def running(self):
        for mode in cycle(self.__modes):
            self.__color = mode[0]
            print(self.__color)
            time.sleep(mode[1])

    def manual_running(self):
        if self.__light_start + dict(self.__modes)[self.__color] <= time.time():
            self.__color = self.__modes[self.__next_light][0]
            self.__light_start = time.time()
            self.__next_light = self.__next_light + 1 if len(self.__modes) > self.__next_light + 1 else 0
        return self.manual_running()


if __name__ == '__main__':
    lighter = TrafficLight()
    lighter.running()
    # for color in lighter:
    #     print(color)
    #     time.sleep(1)
