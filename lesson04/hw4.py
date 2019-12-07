"""
4) Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке
их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
"""
from collections import Counter

massiv = [1, 2, 4, 5, 6, 2, 5, 2]

counter = Counter(massiv)

single = [x for x, n in counter.items() if n == 1]
print(single)


# ниже решение преподавателя
def unique_gen(*args):
    for itm in args:
        if args.count(itm) == 1:
            yield itm


test_list = [1, 2, 3, 4, 5, 1, 4, 3, 6, 3]
result = [itm for itm in test_list if test_list.count(itm) == 1]
