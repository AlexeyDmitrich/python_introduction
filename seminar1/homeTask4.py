 # Петя, Катя и Сережа делают из бумаги журавликов. 
 # Вместе они сделали S журавликов. 
 # Сколько журавликов сделал каждый ребенок, если известно, что 
 # Петя и Сережа сделали одинаковое количество журавликов, а 
 # Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
 
bird_count = int(input("Сколько журавлей сделали дети? \n"))
petya_score = 0
serega_score = 0
katya_score = 0
real_bird_count = bird_count

if (bird_count < 6):
    print ("Дети завалили смену и не выдали даже минимальный план")
    exit()
    
if (bird_count%2 != 0 or bird_count%4 != 0):
    print(f"При соблюдении условий трудозатрат детей невозможно достичь общего числа изделий в {bird_count}")
    while (real_bird_count%2 != 0 or real_bird_count%4 != 0):
        real_bird_count -= 1
    print(f"Скорее всего дети собрали {real_bird_count} журавлей, ещё {(bird_count-real_bird_count)} им дописала добрая табельщица \n в таком случае:")

go = 0
while (go<real_bird_count):
    petya_score += 1
    serega_score += 1
    katya_score = (petya_score+serega_score)*2
    go = petya_score+katya_score+serega_score
#    print (f"Петя: {petya_score}\nСерёжа: {serega_score}\nКатя: {katya_score}\n Общее количество: {go}")
# if (go > bird_count):
#        print("На ввод отправлены ошибочные данные")
else:
    print (f"Петя сделал {petya_score} журавлей, \nСерёжа собрал {serega_score} птиц, \nКатя применила автоматизацию и зафигачила {katya_score} изделий")
