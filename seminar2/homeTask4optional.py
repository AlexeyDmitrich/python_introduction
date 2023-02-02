# задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

limit = int(input("Введите число k \n"))

a = 0
b = 1
c = 2
fib = [a, b, c]
k = 0
while not (k == limit-3):
    fib.append (c+b)
    a = b
    b = c
    c = a+b
    k += 1
    
print(fib)

contr_fib = []
i = 1
while (i<len(fib)):
    contr_fib.append ((fib[-i])*-1)
    contr_fib.append (fib[-i-1])
    i += 2
contr_fib.pop(-1)
print(contr_fib)
 
hyper_fib = []
for num in contr_fib:
    hyper_fib.append(num)
for pos_num in fib:
    hyper_fib.append(pos_num)
    
print(hyper_fib)