# Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) .
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25,
# сами значения предикатов случайные, проверяем это утверждение 100 раз, 
# с помощью модуля time выводим на экран , сколько времени отработала программа. 
# В конце вывести результат проверки истинности этого утверждения.

from random import randint as rnd
import time as tm

def predicates ():
    predicates_right = []
    predicates_left = []
    length = rnd(5,25)
    for predicat in range(length):
        new = rnd(0,1)
        if (new == 1):
            predicates_left.append (True)
        else:
            predicates_left.append (False)
        
    for i in range(length): 
        predicates_right.append (predicates_left[i])

    return(predicates_left, predicates_right)
    
    
def proof (predicates_left, predicates_right):
    conunction = False # True
    disunction = False # True

    for predicat in predicates_left:
        if (not(predicat == True)):   # ни один предикат не true
            disunction = True
            continue
        else:
            disunction = False       # если попадется предикат - true, вернём фолс
    for predicat in predicates_right: 
        if ((not predicat) == True):   # каждый непредикат обязательно true
            conunction = True
            continue        
        else:
            conunction = False   # если хотя бы один непредикат - false, возвращаем фолс

    truthfulness = False
    if conunction == disunction:
        truthfulness = True
    return truthfulness
    
    '''
    Кажется, я что-то упускаю. На одиночной проверке показатель времени был выше, чем в цикле из 100 проверок.
    '''
    
i = 0
start = tm.time()
while (i<100):
    left, right = predicates()
    proofed = proof (left, right)
#    print (proofed)
    if (proofed == False):
        print ("Проверка провалена")
        break
    else:
        i += 1
#        print (f"{i} проверка пройдена")
        continue
print ("Все проверки пройдены успешно")
finish = tm.time()
long = finish-start

print(f"Времени затрачено: {long} с.")
