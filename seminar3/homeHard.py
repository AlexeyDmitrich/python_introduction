# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
'''
from random import randint

n = int(input('Введите размер списка: '))
deck = [randint(1, 10) for i in range(n)]
print(deck)

combination = 1
value = []
hand = {}
for i in range(len(deck)):
    for card in range(len(deck)):
        step = 1
    #    while (card+step < len(deck) and (card+step == card+1 or card+step == card-1)):
        while ((card+step < len(deck) and card-step >= 0)(card+step == card or card-step == card)):
            value.append(card)
            step += 1
        else:
            hand [combination] = value
            step = 0
            combination += 1
        print(hand)
########
from random import randint

n = int(input('Введите размер списка: '))
deck = [randint(2, 14) for i in range(n)]
print(deck)

combination = 1
value = []
hand = {}
for i in range(len(deck)):
    print(f"place {i} : nominal {deck[i]}")
    for card in deck:
        print(f" card {card}")
        step = 1
        while (step < len(deck)): # and (i - step >= 0)):
            print(f"  combination: {combination}\n  step: {step}\n  card nominal: {card}\n  deck[i]-step: {deck[i]-step}\n  deck[i]+step: {deck[i]+step}")
            value.append(deck[i])
            if (deck[i] == card-step):
                print("         TRUE")
                 
                value.append(card)
                step += 1
            #    continue
            if (deck[i] == card+step):
                print("         TRUE")
            #    value.append(deck[i]) 
                value.append(card)
                step += 1
            #    continue
            else:
                print("         FALSE")
                step = 1 
                break
        
    hand [combination] = set(value)
    value = []
    combination += 1
    print(hand)
    '''    

    # #    while (card+step < len(deck) and (card+step == card+1 or card+step == card-1)):
    #         while (step<len(deck) and combination<=len(deck)):
    #             print(f"  combination: {combination}\n  step: {step}\n  card nominal: {card}\n  deck[i]-step: {deck[i]-step}\n  deck[i]+step: {deck[i]+step}")
    #             if ((card==deck[i]-step) or (card==deck[i]+step)):
    #                 print("   TRUE")
    #                 value.append(card)
    #                 step += 1
    #                 print(f"    card appended in value: {value}\n   step up: {step}")
    #                 hand [combination] = value
    #                 print(f"       добавлена пара ключ-значение: {hand}")
    #             #else: 
    #                 #print(f"{combination}")
    #                 #continue
    #             else:

    #                 step = 1
    #                 print(f"       step reset to {step}")
    #                 combination += 1
    #                 print(f"       look at next combination {combination}")
    #                 continue


from random import randint

n = int(input('Введите размер списка: '))
arr = [randint(2, 14) for i in range(n)]
print(arr)


value = []
hands = []
deck = []
for card in (set(arr)):
    deck.append(card)
        
for card in deck:
    hands.append(set())
print (hands)
print (type(hands[0]))
print (deck)
print (type(deck))
print (type(deck[0]))
# exit()
# distance = 1

for i in range(len(deck)):
    hands[i].add(deck[i])
    print (f"добавлено начало последовательности {deck[i]}")
    distance_up = 1
    distance_down = 1
    print ('дистанция сброшена')
    for j in range(len(deck)):
        print (f"ищем el {deck[i]} + dis {distance_up} = {deck[i]+distance_up} в {deck}")
        if (deck[i]+distance_up) in deck:
            print ("найдено")
            hands[i].add(deck[i]+distance_up)
            print (f"добавляем {deck[i]+distance_up} в {hands[i]}")
            distance_up += 1
            print (f"устанавливаем дистанцию увеличения: {distance_up}")
        print (f"ищем el {deck[i]} - dis {distance_down} =  {deck[i]-distance_down} в {deck}")    
        if (deck[i]-distance_down) in deck:
            print ("найдено")
            hands[i].add(deck[i]-distance_down)
            print (f"добавляем {deck[i]-distance_down} в {hands[i]}")
            distance_down += 1
            print (f"устанавливаем дистанцию уменьшения: {distance_down}")

for 


print (hands)
