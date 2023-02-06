# Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]


from random import randint

n = int(input('Введите размер списка: '))
arr = [randint(2, 14) for i in range(n)]
#print(arr)


max_hands = []
hands = []
deck = []
# for card in (set(arr)):
#     deck.append(card)
deck = arr        
for card in deck:
    hands.append(set())
#print (hands)
#print (type(hands[0]))
print (deck)
# print (type(deck))
# print (type(deck[0]))
# exit()
# distance = 1

for i in range(len(deck)):
    hands[i].add(deck[i])
#    print (f"добавлено начало последовательности {deck[i]}")
    distance_up = 1
    distance_down = 1
#    print ('дистанция сброшена')
    for j in range(len(deck)):
#        print (f"ищем el {deck[i]} + dis {distance_up} = {deck[i]+distance_up} в {deck}")
        if (deck[i]+distance_up) in deck:
#            print ("найдено")
            hands[i].add(deck[i]+distance_up)
#            print (f"добавляем {deck[i]+distance_up} в {hands[i]}")
            distance_up += 1
#            print (f"устанавливаем дистанцию увеличения: {distance_up}")
#        print (f"ищем el {deck[i]} - dis {distance_down} =  {deck[i]-distance_down} в {deck}")    
        if (deck[i]-distance_down) in deck:
#            print ("найдено")
            hands[i].add(deck[i]-distance_down)
#            print (f"добавляем {deck[i]-distance_down} в {hands[i]}")
            distance_down += 1
#            print (f"устанавливаем дистанцию уменьшения: {distance_down}")

max_hand = {0}
for hand in hands:
    if len(hand) == len(max_hand):
        max_hands.append(hand)
    if len(hand) > len(max_hand):
        max_hand = hand
        max_hands = []
        max_hands.append(max_hand)
print (max_hand)


for hand in max_hands:
    values = []
    for i in hand:
        values.append(i)
        values.sort()
    print (f'Возможная последовательность: {values[0]}, {values[-1]}')
