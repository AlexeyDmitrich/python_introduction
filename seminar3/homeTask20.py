# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12


score1 = ('a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т')
score2 = ('d', 'g', 'д', 'к', 'л', 'м', 'п', 'у')
score3 = ('b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я')
score4 = ('f', 'h', 'v', 'w', 'y', 'й', 'ы')
score5 = ('k', 'ж', 'з', 'х', 'ц', 'ч')
score8 = ('j', 'x', 'ш', 'э', 'ю')
score10 = ('q', 'z', 'ф', 'щ', 'ъ')
    
world = input("Введите слово: ")
score = 0
for char in world.lower():
#    print (char)
    if char in score1:
        score += 1
        print(f"за букву {char.upper()} начислено 1 очко. всего набрано: {score}")
    elif char in score2:
        score += 2
        print(f"за букву {char.upper()} начислено 2 очка. всего набрано: {score}")
    elif char in score3:
        score += 3
        print(f"за букву {char.upper()} начислено 3 очка. всего набрано: {score}")
    elif char in score4:
        score += 4
        print(f"за букву {char.upper()} начислено 4 очка. всего набрано: {score}")
    elif char in score5:
        score += 5
        print(f"за букву {char.upper()} начислено 5 очков. всего набрано: {score}")
    elif char in score8:
        score += 8
        print(f"за букву {char.upper()} начислено 8 очков. всего набрано: {score}")
    elif char in score10:
        score += 10
        print(f"за букву {char.upper()} начислено 10 очков. всего набрано: {score}")

print(f'Всего Вы набрали {score} очков')