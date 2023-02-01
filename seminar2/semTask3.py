# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2.
# from random import randint as rnd

# n = int(input("введите число рассматриваемых дней от 1 до 100"))
# temper_lst = []
# count = 0
# count_max = 0
# for i in range (n):
#     temper_lst.append (rnd(-50,50))
# for j in range(len(temper_lst)):
#     if temper_lst[j]>0:
#         while not ((temper_lst[j]<0) or (j>=n)):
#             count += 1
#             j+=1
#             if temper_lst[j]<0:
#                 if count > count_max:
#                     count_max = count
#                     count = 0

# print(f"В графике температур {temper_lst} \n максимальная оттепель составила {count_max} дней")

import random

while True:
    n = input('Введите число дней N или "Q" для выхода:')
    if n == 'Q':
        exit()

    n = int(n)
    temp_stat = []

    for _ in range(n):
        temp_stat.append(random.randint(-50, 50))

    print(temp_stat)

    count = max_count = 0

    for temp in temp_stat:
        if temp > 0:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0

    print(max_count)