# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

progressive_array = []
first_element = int(input("Введите первый элемент\n"))
difference = int(input("Введите разность\n"))
limit = int(input("Сколько элементов должно быть\n"))

def fill_progress_list (users_list, first=0, difference=1, limit=10):
    if limit == 0:
        return users_list
    users_list.insert(0, first+(limit-1)*difference)
    return fill_progress_list (users_list, first, difference, limit-1)

print(fill_progress_list(progressive_array, first_element, difference, limit))
