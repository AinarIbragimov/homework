"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

f=open('hw5_test.txt','w')
a = ['10 ', '15 ', '20']
f.writelines(a)
f.close()

with open('hw5_test.txt','r') as file:
    s = file.readline()
s = list(map(int, s.split()))
print(sum(s))





