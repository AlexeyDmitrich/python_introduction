# Задача No49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import json as js
phone_book = []

def save ():
    try:
        with open ('phoneBook.json', 'w', encoding='UTF-8') as pb:
            pb.write(js.dumps(phone_book, ensure_ascii=False))
            print ('Сохранили')
    except:
        print('Не удалось сохранить :(')

def load ():
    global phone_book
    try:
        with open ('phoneBook.json', 'r', encoding='UTF-8') as pb:
            phone_book = js.load(pb)
    except: 
        print('У Вас ещё нет телефонной книги. Создаем.')
#        save()
        
def add_abonent ():
    phone_note = ['','','',[]]
    surname = input('Введите фамилию\n')
    name = input('Введите имя\n')
    secondname = input('Введите отчество\n')
    phone_note[0]=(surname)
    phone_note[1]=(name)
    phone_note[2]=(secondname)
    number = ' '
    while number != '':
        number = input ('Введите номер телефона и нажмите enter, если номеров больше нет, просто нажмите enter')
        if number != '':
            phone_note[3].append(number)
    phone_book.append(phone_note)
    return menu()

def show_all ():
    print(phone_book)
    # for phone_note in phone_book:
    #     print (phone_note)
        
def menu():
    while True:
        choise = input('выберите чё делать')
        match (choise):
            case '1':
                add_abonent()
            case '2':
                show_all()
            case '3':
                save()
            case '0':
                yes = 'сохранитьдавайугуагаможнонаверноехзмбyesyeahsave'
                request = input("Сохранить сеанс перед выходом?\n")
                if request.lower() in yes:
                    save()
                print ('До новых встреч!')
                exit()
load()
menu()   