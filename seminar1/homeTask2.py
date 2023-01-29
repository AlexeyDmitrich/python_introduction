#Найдите сумму цифр трехзначного числа.

number = int(input("Введите целое число \n")) # или не трёхзначное ?
sum_of_digits = 0

if (number < 0):
    number_clone = -number
else:
    number_clone = number
    
while (number_clone>0):
    sum_of_digits += (number_clone % 10)
#    print(f"Исходник: {number} \n Текущая сумма: {sum_of_digits}")
    number_clone //= 10 
#    print(f"Исходник: {number_clone} \n Текущая сумма: {sum_of_digits}")

print(f"Сумма цифр числа {number} составит {sum_of_digits}")