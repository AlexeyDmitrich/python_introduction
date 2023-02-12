# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

users_num_a = int(input("Введите число a: \n"))
users_num_b = int(input("Введите число b: \n"))

def involution (number_a, number_b):
    if number_b == 0:
        return number_a
    return involution (number_a+1, number_b-1)

res = involution(users_num_a, users_num_b)
print(res)