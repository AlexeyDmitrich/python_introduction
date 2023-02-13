# Даны два массива чисел. Требуется вывести те элементы
# первого массива(в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива


from random import randint


def compare(sp1, sp2):
    sp = []
    for i in sp1:
        if i not in sp2:
            sp.append(i)
    print(sp)


try:
    while True:
        n = int(input('Введите количество 1: '))
        lst1 = [randint(1, 9) for _ in range(n)]
        print(lst1)
        m = int(input('Введите количество 2: '))
        lst2 = [randint(1, 9) for _ in range(m)]
        print(lst2)
        compare(lst1, lst2)
        print()
except:
    print('Введены некорректные данные.\nВыход из программы.')
exit()