ur_number = int(input("Введите юридический номер вагона (тот, который написан на стенке вагона) \n"))
count_number = int(input("Введите номер вагона от головы состава \n"))

if (ur_number == count_number):
    print ("Для определения количества вагонов не хватает данных")
else:
    amount = ur_number+count_number-1
    print (f"Мы насчитали {amount} вагонов в составе")