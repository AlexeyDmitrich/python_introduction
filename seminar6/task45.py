# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

def friendly_nums (parced_num):
    sum_div = 0
    div = parced_num-1
    while not(div == 1):
        if parced_num % div == 0:
            sum_div += div
    return sum_div
    
def is_friendly (num1, num2):
    if num1 != num2 and friendly_nums(num1) == num2 and friendly_nums(num2) == num1:
        return True

max_num = int(input("Введите число ограничитель: /n"))

while max_num > 0:
    max_num 


exit()

def getSum(value):
    res = 1
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            res += i + value // i
    return res

for i in range(10, 3000):
    sum1 = getSum(i)
    sum2 = getSum(sum1)
    if sum2 == i and sum1 != sum2:
        print(i, sum1)