# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
'''
from random import randint

n = int(input('Введите размер списка: '))

lst = [randint(1, 10) for i in range(n)]
print(lst)
'''
from random import randint

n = int(input('Введите размер списка: '))
deck = [randint(1, 10) for i in range(n)]
print(deck)

combination = 1
value = []
hand = {}
for i in range(len(deck)):
    for card in range(len(deck)):
        step = 1
    #    while (card+step < len(deck) and (card+step == card+1 or card+step == card-1)):
        while ((card+step < len(deck) and card-step >= 0)(card+step == card or card-step == card)):
            value.append(card)
            step += 1
        else:
            hand [combination] = value
            step = 0
            combination += 1
        print(hand)
