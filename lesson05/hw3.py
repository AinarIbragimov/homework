"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

# создаем текстовый файл и пишем текст
f = open("hw3_test.txt", "w")
workers = ['Ivanov: 15000\n', 'Petrov: 18000\n', 'Basharov: 25000\n', 'Sidorov: 30000\n']
f.writelines(workers)

a = '''Ivanov — 15000
Petrov — 18000
Basharov — 25000
Sidorov — 30000
'''
f.close()

from functools  import reduce
with open('hw3_test.txt', 'r', encoding='utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')

        # new_list = list(map(lambda y: sum(int(y)), value))
        # print(new_list)

        # value = int(value)
        # a = sum(int(value))/len(value)
        # print(a)
# Выполнить подсчет средней величины дохода сотрудников не знаю как???

