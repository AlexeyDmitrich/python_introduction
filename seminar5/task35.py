# Задача No35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

users_number = int(input("Введите число\n"))

def is_simple (number, div=users_number-1):
    if div == 1:
        return True
    if number % div == 0:
        return False
    return is_simple (number, div-1)

res = is_simple (users_number)
print(res)