# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A i. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint as rnd

def gen_array (size):
    array = []
    n=1
    while (n <= size):
        array.append(rnd(1, size))
        n += 1

    return(array)

def find_neighbor_number (array, num):
    searched_num = num
    distance = 1
    for i in array:
        if (searched_num == i):
            print("В списке есть и оригинал, если что")
            break
    for i in range(len(array)):
        print(f'   iteration:{i}\n   ')
        if ((searched_num + distance) == array[i]):
            print(array[i])
            return array[i]
        elif ((searched_num - distance) == array[i]):
            print(array[i])
            return array[i]
        else:
            distance += 1    


try:
    array_size = int(input("Введите количество элементов для обработки\n"))
except:
    print("Этим точно можно что-то посчитать?")

try:
    startpoint_num = int(input("Введите число, соседа которого нужно найти\n"))
except:
    print("Там однозначно нет такого")

working_array = gen_array(array_size)
print(working_array)
neighbor = find_neighbor_number(working_array, startpoint_num)

print(f"Ближайшее число к искомому {startpoint_num}, это {neighbor}")