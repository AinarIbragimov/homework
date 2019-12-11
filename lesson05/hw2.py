"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
# создаем текстовый файл и пишем текст
f = open("hw2_test.txt", "w")
str_list = ('I want to save this is several string text and \n to made calculation number of lines, \n '
            'the number of words in each row')
f.writelines(str_list)
f.close()

# считываем с файла текст во всех строках
f = open('hw2_test.txt')
lines = f.readlines()

# создаем другой файл, куда будем переводить информацию о количестве строк в тексте и слов в каждой строке
with open('hw2_test2.txt', 'w') as ff:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        ff.write('Line number {} has {} words.\n'.format(index + 1, number_of_words))

# результат также печатаем здесь
with open('hw2_test2.txt', 'r', encoding='ascii') as ff:
    print(ff.read())
