"""
2) Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
"""


# my_list = [2, 4, 8, 1, 9, 3, 1]
# print(f"исходный список: {my_list}")
# new_list = []
# for el in my_list:
#     new_list.append(el + 7)
# print(f"Новый список: {new_list}")
# # Я в новый список прибавил ко всем значениям число 7. Изначально я так понял задание.


def test_iter(*args):
    prev = float('inf') * -1

    for idx, itm in enumerate(args):
        if itm > prev:
            yield itm
        prev = itm


if __name__ == '__main__':
    assert list(test_iter(1, 2, 3, 4, 5, 6, 7, 8)) == [1, 2, 3, 4, 5, 6, 7, 8], 'one'
    assert list(test_iter(-1, 3, 6, 12, -5, 0, 2, 7)) == [-1, 3, 6, 12, 0, 2, 7], 'two'
    assert list(test_iter(1)) == [], 'three'
    assert list(test_iter()) == [], 'four'
