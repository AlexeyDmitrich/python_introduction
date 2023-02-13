# Задача №43. Общее обсуждение
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

from random import randint as rnd

users_len_list = int(input("Введите предполагаемую длину массива \n"))
users_list = []

for i in range(users_len_list):
    users_list.append(rnd(1,10))

def find_pairs_in_list (users_list):
    count = 0
    for i in range(len(users_list)):
        for j in range(i+1,len(users_list)):
            if users_list[i] == users_list[j] and users_list[j] != '' and users_list[i] != '':
                count+=1
                users_list[j] = ''
                users_list[i] = ''
    return count
    
print(users_list)
res = find_pairs_in_list(users_list)
print (res)

exit()

# Задача №43. 
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 1 2 3 2 3 
# Вывод: 2



a = list(map(int, input('Введите числа списка через пробел: ').split()))
counter = 0
a1 = set(a)
a2 = []
for i in (a1):
    for j in range(0, len(a)):
        if i == a[j]:
            counter += 1
    a2.append(counter)
    counter = 0 
counter2 = 0
for i in range(len(a2)):
    counter2 = counter2 + a2[i]//2


print(counter2)