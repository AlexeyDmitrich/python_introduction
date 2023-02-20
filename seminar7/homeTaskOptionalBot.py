# сделать локальный чат-бот с хранилищем данных в формате JSON, как объясняли в приложенной записи буткемпа.


import json as js

base_of_skills = [] # список коротких строк
base_of_vacancis = []  # список списков/словарь (или т.п.). Уместить: должность - скиллы - уровень соответствия

def load ():
    try:
        with open ('skills.json', 'r', encoding='UTF-8') as sk:
            base_of_skills = js.load(sk)
            print ('база навыков загружена')
        with open ('vacancy.json', 'r', encoding='UTF-8') as vac:
            base_of_vacancis = js.load(vac)
            print ('база вакансий загружена')
    except:
        print ("Сохранённый сеанс отсутствует. Это ничего, сейчас создадим.")
        save()
        print ('Готово, ботом можно пользоваться')

def save ():
    try:
        with open ('skills.json', 'w', encoding='UTF-8') as sk:
            sk.write (js.dumps (base_of_skills, ensure_ascii=False))
            print ("База навыков успешно сохранена")
    except:
        print ("Не удалось сохранить новые навыки")
    try:
        with open ('vacancy.json', 'w', encoding='UTF-8') as vac:
            vac.write (js.dumps (base_of_vacancis, ensure_ascii=False))
            print ("База вакансий успешно сохранена")
    except:
        print ("Не удалось сохранить новые вакансии")
    
def translator (users_text):
    start = ''
    stop = ''
    help = ''
    addvac = ''
    addskill = ''
    rate = ''
    if str(users_text).lower in start:
        return '/start'
    if str(users_text).lower in start:
        return '/start'


def wokring ():
    while True:
        choise = input("Введите команду \n")
        # choise = translator(choice) TODO: translator
        match (choise):
            case '/start':
                print ('Добро пожаловаться')
                load()
            case '/stop':
                yes = 'даугуагаможнонаверноеyesyeah'
                request = input("Сохранить сеанс перед выходом?")
                if str(request).lower in yes:
                    save()
                break
            case '/help':
                print ('здесь появится раздел помощи')
            case '/addvac':
                print ('раздел в разработке')
                # TODO: function to add vacancy in base_of_vacancis
            case '/addskill':
                print ('раздел в разработке')
                # TODO: function to add skill in base_of_skills
            case '/rate':
                print ('раздел в разработке')
                # TODO: function calc worker rate to job
