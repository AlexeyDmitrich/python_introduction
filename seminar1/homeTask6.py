# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

try:
    ticket_number = int(input("Введите номер билета \n"))
except:
    print("Давайте сразу договоримся считать номером билета шестизначное натуральное число")
    exit()

if (ticket_number < 100000 or ticket_number > 999999):
    print("Нужен шестизначный номер без букав и пробелов. Обычно сверху на билете пишется")
    exit()

first_half = ticket_number//1000
#print(first_half)
second_half = ticket_number - first_half*1000
#print(second_half)

def sum_of_digits (number):
    sum = 0
    while (number > 0):
        sum += number%10
        number = number // 10
#        print(number)
    return sum

first_half_sum = sum_of_digits(first_half)
# print (first_half_sum)
second_half_sum = sum_of_digits(second_half)
# print (second_half_sum)

if (first_half_sum == second_half_sum):
    print ("Вам повезло, билет оказался счастливым")
else:
    print ("Билет как билет, ну, может в другой раз")