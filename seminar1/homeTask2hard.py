# Найдите сумму цифр любого вещественного или целого числа. 
# Можно использовать decimal. Через строку решать нельзя. 

try:
    number = float(input("Введите число \n"))
except:
    print ("Это точно число?")

if (number < 0):
    number *= -1

integer_number = number
while (integer_number % 10 != 0):
    integer_number *= 10
print(integer_number)

integer_number = int(integer_number)

digit_sum = 0
while (integer_number > 0):
    digit_sum += integer_number%10
    integer_number //= 10
    
print(f"Сумма всех цифр числа {number} равна {digit_sum}")