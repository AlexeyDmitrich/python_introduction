# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

users_num = int(input("Введите число, которое будем возводить в степень: \n"))
users_expo = int(input("Введите степень, в которую нужно возвести число: \n"))

def involution (raised_number, raised_number_static, exponention):
    if exponention == 1:
        return raised_number
    return involution (raised_number*raised_number_static, raised_number_static, exponention-1)

res = involution(users_num, users_num, users_expo)
print(res)