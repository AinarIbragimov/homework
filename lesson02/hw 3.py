"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

# Реализуем через dict:
my_dict = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
# просим пользователя ввести число от 1 до 12
month = int(input('Укажите месяц от 1 до 12: '))
for key in my_dict.keys():
    if month in my_dict[key]:
        print(key)

# # Реализовать через list пока не удалось