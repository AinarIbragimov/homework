"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""

def my_func():
    num1 = int(input('Введите число №1 '))
    num2 = int(input('Введите число №2 '))
    num3 = int(input('Введите число №3 '))
    numbers = (num1, num2, num3)
    # находим сумму всех числе
    sum_1 = (sum(numbers))
    # находим минимальное значение
    min_1 = (min(numbers))
    # вычитаем из суммы минимальное
    num4 = sum_1 - min_1
    return num4

a = my_func()
print(a)