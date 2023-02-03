# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint as rnd


def distribution ():
    table = []
    table_limit = int(input("Введите ограничение по максимальному числу монет \n"))
    table_size = rnd(1, table_limit)
    for i in range (table_size):
        table.append(rnd(0,1))
    return table

def heads_or_tails (table):
    heads_counter = 0
    tails_counter = 0
    for coin in table: 
        if (coin == 0):
            tails_counter += 1
#            print(coin, "tails", tails_counter)
        else:
            heads_counter += 1
#            print(coin, "heads", heads_counter)            
    if (heads_counter == tails_counter):
        return(heads_counter, "(любых)")
    elif (heads_counter > tails_counter):
        return(tails_counter, "с решкой")
    else:
        return(heads_counter, "лежащих орлом вверх")
        
        

table = distribution()
#print(table)
counter, nominal = heads_or_tails (table)
# print(nominal)
# print(counter)


for i in range(int(len(table))):
    if (table[i] == 1):
        table[i] = ("О")
    else:
        table[i] = ("Р")
print(table[:4])
print(table[4:8])
print(table[8:12])
print(table[12:16])
print(table[16:])

print(f"Нужно перевернуть {counter} монет {nominal}")
