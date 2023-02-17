# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(characteristic, objects):
    # проверяем пустой массив
    result = True
    if (len(objects) == 0):
        return result
    
    # применяем переданную функцию на все элементы
    res = list(map(characteristic, objects))
    
    # берем значение первого элемента и сравниваем со значениями всех жлементов
    first = res[0]
    check = len(list(filter(lambda x: x == first, res)))
    print(res)
    print(check)

    # выдаем True, когда количество элементов после сравнения совпадает с количеством входных элементов массива
    return check == len(objects)

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
    
    
exit()

values = [0, 2, 11, 6]

def same_by(characteristic, objects):
    # return len(set(map(characteristic, objects)))
    s = set([characteristic(x) for x in objects])
    if len(s) == 1:
        return True 
    else:
        return False

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')