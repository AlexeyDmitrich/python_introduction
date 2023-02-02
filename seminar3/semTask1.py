# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

'''
from random import randint as rnd
ls_of_numbers = []
for num in range(rnd(10, 100)):
    ls_of_numbers.append (rnd(-8, 8))
print(ls_of_numbers)

unicue = []
for i in ls_of_numbers:
    for j in ls_of_numbers:
        if ls_of_numbers[i]==ls_of_numbers[j]:
            continue
        else:
            unicue.append(ls_of_numbers[i])
print(unicue)
'''

from random import randint

n = int(input('Введите размер списка: '))

lst = [randint(-5, 10) for i in range(n)]
print(lst)

lst2 = set(lst)
print(len(lst2))