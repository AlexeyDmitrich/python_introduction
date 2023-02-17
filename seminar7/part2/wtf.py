example_string = "аяуюоеёэиы"
list_str = "пара-ра-рам рам-пам-папам па-ра-па-дам".split()
list_len = []

for one_str in list_str:
    list_vowels = [vowels for vowels in one_str if vowels in example_string] # [a,a,a,a]
list_len.append(len(list_vowels))

print("Парам пам-пам" if len(set(list_len)) == 1 else "Пам парам") 