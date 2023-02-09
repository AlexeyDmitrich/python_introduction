# Задача No31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

number = int(input("Введите число-ограничитель"))

def fibonacci (num_k):
    if num_k in [1, 2]:
        return num_k-1
    return fibonacci(num_k-1)+fibonacci(num_k-2)
    
res = fibonacci(number)
print(res)