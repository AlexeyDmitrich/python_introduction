speed = int(input("Введите скорость в киломеетрах в день \n"))
distance = int(input("Введите расстояние \n"))

if (distance%speed != 0):
    time = distance//speed+1
else:
    time = distance//speed


print (time) 
