# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint as rnd


def distribution ():
    table = []
    table_limit = int(input("Введите ограничение по максимальному числу монет"))
    table_size = rnd(1, table_limit)
    for i in range (table_size):
        table.append(rnd(0,1))
    return table

def heads_or_tails (table):
    heads_counter = 0
    tails_counter = 0
    for coin in range(len(table)):
        if (coin == 0):
            tails_counter += 1
        if (coin == 1):
            heads_counter += 1
            
    ##
        
        

table = distribution()
print(table)