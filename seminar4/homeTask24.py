# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

'''
1) "замкнутый" список
1*) расположен во входном файле
2) максимальная сумма по трём последовательным элементам
'''

from random import randint as rnd

def make_gardenbed (file):
    new_bed = []
    bed_size = int(input("Определите размер грядки: "))
    for bush in range(bed_size):
        new_bed.append(rnd(0,150))

    try:
        bed = open(file, "w")
        try:
            for bush in new_bed:
                bed.write(f"{bush} ")
        except Exception as e:
            print(e)
        finally:
            bed.close()
    except Exception as ex:
        print(ex)

def parce_gardenbed (file):
    bed_as_circ_list = []
    try:
        bed = open(file, "r")
        try:
            bed_string = (bed.readline()).split()
            print (f"{bed_string}")
            for bush in bed_string:
                bed_as_circ_list.append(int(bush))
            bed_as_circ_list.append(bed_as_circ_list[0])    # ровная круглая грядка замыкается
            bed_as_circ_list.append(bed_as_circ_list[1])    # здесь происходит зацикливание списка
        except Exception as e:
            print(e)
        finally:
            bed.close()
    except Exception as ex:
        print(ex)
    return bed_as_circ_list

make_gardenbed("gardenbed.txt")
circle_bed = parce_gardenbed("gardenbed.txt")
#print(circle_bed)
max_harvest = 0
harvest = 0
for i in range(1, len(circle_bed)-1):
    harvest = circle_bed[i-1]+circle_bed[i]+circle_bed[i+1]
    if harvest > max_harvest:
        max_harvest = harvest
        index = i
#        print(f"*********\nпред: {i-1} ({circle_bed[i-1]}) \nточка сбора: {i} ({circle_bed[i]}) \nслед: {i+1} ({circle_bed[i+1]}) \n------------\n  сум: {harvest}")
print (f"Оптимальная точка сбора: {index} куст. \n будет собрано {max_harvest} ягоды \n ({circle_bed[index-1]}+{circle_bed[index]}+{circle_bed[index+1]})") 
