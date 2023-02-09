# Задача No37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

from random import randint as rnd
users_number = int(input("Введите число\n"))

rand_list = []

def fill_list (users_lst, size):
    if len(users_lst) == size:
        return users_lst
    else: 
        users_lst.append(rnd(2,30))
        return fill_list (users_lst, size)

fill_list (rand_list, users_number)
print (rand_list)

'''
n = int(input('Введите N: '))

def addWord(ind, str):
    if (ind >= n):
        return str
    str += input(f'Введите {ind+1}-ый символ: ')
    return addWord(ind +1, str)

def revertStr(ind, inputStr, resultStr):
    if (ind < 0):
        return resultStr
    resultStr += inputStr[ind]
    return revertStr(ind -1, inputStr, resultStr)

inputStr = addWord(0, "")
torevertStr = revertStr(len(inputStr) -1, inputStr, "")
print(inputStr)
print(torevertStr)
'''