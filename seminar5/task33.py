# Задача No33. Решение в группах
# Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint as rnd
volume = int(input("Задайте кольчество оценок"))
arr_grade = []
#[randint(1,5) for _ in range(10)]
for i in range(volume):
    arr_grade.append(rnd(1,5))

print(arr_grade)

def max_val(array):  
    if len(array)>1:
        max = max_val(array[1:])
        if array[0]< max:
            return max
        else:
            return array[0]
    if len(array)==1: 
        return array[0] 
    
def min_val(array):  
    if len(array)>1:
        min = min_val(array[1:])
        if array[0]> min:
            return min
        else:
            return array[0]
    if len(array)==1: 
        return array[0] 


def fail_marks (grades, index):
    max = max_val(grades)
    min = min_val(grades)
    max = min
    if index < len(grades):
        return
    
    
    '''
    n = int(input('Введите количество оценок: '))

grades = [randint(1, 5) for _ in range(n)]
print(grades)
max_grade = max(grades)
min_grade = min(grades)

i = 0
def change_grades(grades, max_grade, min_grade, i):
    if i == len(grades):
        return grades
    else:
        if max_grade == grades[i]:
            grades[i] = min_grade
    return change_grades(grades, max_grade, min_grade, i + 1)

print(change_grades(grades, max_grade, min_grade, i))
    '''