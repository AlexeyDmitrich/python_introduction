# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint as rnd

# раскладывание монет на стол
def distribution ():
    table = []
    table_limit = int(input("Введите ограничение по максимальному числу монет \n"))
    table_size = rnd(1, table_limit)
    for i in range (table_size):
        table.append(rnd(0,1))
    return table

# подсчёт меньшего количества монет
def heads_or_tails (table):
    heads_counter = 0
    tails_counter = 0
    for coin in table: 
        if (coin == 0):
            tails_counter += 1
        else:
            heads_counter += 1
    if (heads_counter == tails_counter):
        return(heads_counter, "(любых)")
    elif (heads_counter > tails_counter):
        return(tails_counter, "с решкой")
    else:
        return(heads_counter, "лежащих орлом вверх")
        
# красивое раскладывание монет на стол
def table_print (table):
    demo_limit = 4
    static_limit = demo_limit
    while (len(table)%static_limit != 0):
        table.append(" ")
    else:
        for i in range(int(len(table))):
            if (table[i] == 1):
                table[i] = ("О")
            if (table[i] == 0):
                table[i] = ("Р")
    print(table[:demo_limit])
    while (demo_limit <= len(table)):
        print(table[(demo_limit):(demo_limit+static_limit)])
        demo_limit += static_limit
    print(table[demo_limit:])

# запуск методов
table = distribution()
counter, nominal = heads_or_tails (table)
table_print(table)
print(f"Нужно перевернуть {counter} монет {nominal}")