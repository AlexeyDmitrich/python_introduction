# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint

n = int(input('Введите размер списка: '))

lst = [randint(-5, 10) for i in range(n)]
print(lst)

counter = 0
for i in range(1,len(lst)):
    if (lst[i] > lst[i-1]):
        counter += 1

print(counter)