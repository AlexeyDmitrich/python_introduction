# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n

str = input("введите строку")

str = 'a a a b c a a d c d d'
lst = str.split()

print(lst)

count = 0
temp = lst[0]

for i in range(1, len(lst)):
    if len(lst[i]) == 1:
        for v in range(i, len(lst)):
            if temp == lst[v]:
                count += 1
                lst[v] += f'_{count}'
        temp = lst[i]
        count = 0

print(lst)
        