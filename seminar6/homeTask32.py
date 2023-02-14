# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint as rnd
from termcolor import colored as color

print("Формирование первичного списка...")
automatic = input("Сгенерировать список без Вашего участия? y/N")
if automatic in ['y Y yes Yes д Д Да да']:
    start_list = [rnd(-1000, 1000) for _ in range(100)]
else:
    set_min_limit = int(input("Введите минимально допустимое значение:\n"))
    set_max_limit = int(input("Введите максимально допустимое значение:\n"))
    set_size_limit = int(input("Введите минимально допустимый размер массива:\n"))
    start_list = [rnd(set_min_limit, set_max_limit) for _ in range(set_size_limit)]
print(f"\n{start_list}\n")
print("Формирование выборки...")
min_limit = int(input("Введите минимально допустимое значение для выборки:\n"))
max_limit = int(input("Введите максимально допустимое значение для выборки:\n"))

def choise_list (incomming_list, min_limit, max_limit):
    test_list = []
    res_list = []
    for i in range(len(incomming_list)):
        if min_limit <= incomming_list[i] <= max_limit:
            test_list.append(color(incomming_list[i], 'green'))
            res_list.append(i)
        else:
            test_list.append(incomming_list[i])
    print(' '.join(str(num) for num in test_list))
    return res_list

list_in_diap = choise_list(start_list, min_limit, max_limit)
print(f"\nИндексы элементов, попадающих в выборку:\n{list_in_diap}\n")
