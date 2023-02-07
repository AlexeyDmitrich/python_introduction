# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint as rnd

#users_numbers_len = int(input("1st len: "))

def create_set (len):    
    users_numbers = set()
    for i in range (len):
        users_numbers.add(rnd(-100,100))
    return users_numbers

kit1 = create_set(int(input("1st len: ")))
print(kit1)
kit2 = create_set(int(input("2nd len: ")))
print(kit2)
