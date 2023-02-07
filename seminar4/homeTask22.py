# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint as rnd

#users_numbers_len = int(input("1st len: "))

def create_list_of_nums (len):    
    users_numbers = []
    for i in range (len):
        users_numbers.append(rnd(-100,100))
    return users_numbers

def find_mini (lst):
    min = lst[0]
    mini = 0
    for i in range(len(lst)):
        if (lst[i] < min):
            min = lst[i]
            mini = i
    return mini

def unite_lists (part_list1, part_list2):
    part1, part2 = set(part_list1), set(part_list2)
    united_set = part1.union(part2)
    united_list = []
    for element in united_set:
        united_list.append(element)
    return united_list

def sort_to_kit (users_list1, users_list2):
    users_list = unite_lists(users_list1, users_list2)
    sorted_list = []
    while (len(users_list) > 0):
        min = find_mini(users_list)
        sorted_list.append(users_list.pop(min))
    return sorted_list

def run ():
    print("Для выхода введите 0")
    try:    
        kit1 = create_list_of_nums(int(input("Установите длину первого набора чисел: ")))
        print(kit1)
        kit2 = create_list_of_nums(int(input("Установите длину второго набора чисел: ")))
        print(kit2)
    except:
        print("Введено неверное значение")
        run()
    if len(kit1) == 0 or len(kit2) == 0:
        print("Завершение работы программы...")
        exit()

    sorted_kit = sort_to_kit (kit1, kit2)
    print (sorted_kit)

while True:
    run()
