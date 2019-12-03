"""
1) Реализовать скрипт , в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys

if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print("usage : python .....")
        exit(1)

    val1 = int(sys.argv[1])
    val2 = int(sys.argv[2])
    val3 = int(sys.argv[3])
    bonus1 = 3000
    bonus2 = 4000
    bonus3 = 5000
    print('Salary employee1', val1 *200 + bonus1)
    print('Salary employee2', val2 *250 + bonus2)
    print('Salary employee3', val3 *300 + bonus3)

# При вводе через Terminal: hw1.py 10 100 1000   #10,100,1000 - это количество часов.
# Terminal выдаст:
# Salary employee1 5000
# Salary employee2 29000
# Salary employee3 305000
