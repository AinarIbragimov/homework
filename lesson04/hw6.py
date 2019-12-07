"""
6) Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools .
"""

from itertools import count
from itertools import cycle

for el in count(13):
    print(el)

for el in cycle("ABC"):
    print(el)

# Выше моё решение, ниже решение от преподавателя
from itertools import (count,
                       cycle, )

def inf_numbers(start):
    while True:
        yield start
        start += 1

tmp = [1,2,3,4]
cycle_iter = cycle(tmp)
inf_numbers2 = count(2)





