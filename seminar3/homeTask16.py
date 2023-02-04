# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A i. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint as rnd

# функция генерирует массив нужной длины, с числами в диапазоне от 1 до этой длины. 
# Но числа могут стоять в случайном порядке и главное - повторяться, иначе смысл задачи теряется.
def gen_array (size):
    array = []
    n=1
    while (n <= size):
        array.append(rnd(1, size))
        n += 1

    return(array)

# функция пробегается по списку, считает упоминания числа и возвращает их количество
def search_num (array_to_search, searched_num):
    counter = 0
    for num in array_to_search:
        if (num == searched_num):
            counter += 1
    return(counter)

try:
    array_size = int(input("Введите количество элементов для обработки\n"))
except:
    print("Этим точно можно что-то посчитать?")

try:
    searched_num = int(input("Введите число, которое нужно найти\n"))
except:
    print("Там однозначно нет такого")

    
working_array = gen_array(array_size)
print(working_array)
count = search_num(working_array, searched_num)
print(f"{searched_num} используется {count} раз")


