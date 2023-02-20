# сделать локальный чат-бот с хранилищем данных в формате JSON, как объясняли в приложенной записи буткемпа.

import json as js

base_of_skills = [] # список коротких строк
base_of_vacancis = []  # список списков/словарь (или т.п.). Уместить: должность - скиллы - уровень соответствия
# при отдельном пересчете для каждой вакансии - есть ли смысл вводить переменную rate в список значений вакансии?
rate_to_vacancy = {}

def load ():
    try:
        with open ('skills.json', 'r', encoding='UTF-8') as sk:
            base_of_skills = js.load(sk)
            print ('база навыков загружена')
        with open ('vacancy.json', 'r', encoding='UTF-8') as vac:
            base_of_vacancis = js.load(vac)
            print ('база вакансий загружена\n')
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
    start = '/startgoпоехалистартвперёдпогнали'
    stop = '/stopстопостановитьхватитпрекратиуйтивыходвыйтизакончить'
    help = '/helpmanualпомощьпомочьпомогитемануалсправка'
    add = 'добавитьвнестидополнить'
    addvac = '/addvacвакансиивакансиювакант' # тезаурус в разработке
    addskill = '/addskillопытумениепрактикускиллнавык'  # тезаурус в разработке
    rate = '/rate' # тезаурус в разработке
    if str(users_text).lower() in start:
        return '/start'
    if str(users_text).lower() in stop:
        return '/stop'
    if str(users_text).lower() in help:
        return '/help'
    if str(users_text).split()[0].lower() in add:
        if str(users_text).split()[1].lower() in addvac:
            return '/addvac'
        if str(users_text).split()[1].lower() in addskill:
            print(str(users_text).split()[1])
            return '/addskill'
        else:
            print('не удалось обработать запрос')
    if str(users_text).lower() in addvac:
        return '/addvac'
    if str(users_text).lower() in addskill:
        return '/addskill'
    if str(users_text).lower() in rate:
        return '/rate'
    else:
        print('не удалось обработать запрос')

def print_help ():
    print('''
    Бот расчитан на взаимодействие с простыми командами на русском языке,
    сформулированными одним словом.
    Но этот метод ещё в разработке, поэтому, вот перечень основных команд,
    если он не понял по-русски:

    /start \t- начать взаимодействие с ботом
    /addvac \t- добавить вакансию с требованиями в список вакансий
    /addskill \t- добавить свой новый опыт (духовный не учитывается)
    /allvac \t- просмотр имеющихся вакансий
    /allskills \t- просмотр своего опыта
    /rate \t- посмотреть совместимость своего опыта с имеющимися вакансиями
    /stop \t- остановить бота (будет предложено сохранить сеанс)
    /help \t- показать эту страницу помощи
    ''')
    
def add_skill ():
    skill = input('''
    Этот раздел нужен для добавления своего опыта/навыков/знаний/умений, 
    что там ещё у Вас есть. Очень рекомендую для каждого навыка вызывать 
    эту команду отдельно. Позвольте дать Вам ещё совет: вводите название 
    навыка так, как его указывает работодатель в описании вакансии.

    Введите название Вашего опыта:

    ''')

    base_of_skills.append(skill.lower())
    print ('Навык добавлен \n')

def add_vacancy ():
    print ('''
    Здесь всё не так просто, как с добавлением навыков, но, если выполнять все подсказки
    бота - то добавить новую вакансию не составит труда. 
    ''')
    name = input('Для начала введите название вакансии: \n')
    skills = []
    skill = ' '
    rate = 0
    while skill != '':
        skill = input('''
        Введите одно из требований к кандидату и нажмите Enter. 
        Этот вопрос будет задан снова, если требований больше нет,
        просто нажмите Enter \n''')
        if skill != '':
            skills.append(skill.lower())
        if skill in base_of_skills:
            rate += 1
    if rate >= len(skills):
        print('Есть вероятность, что Вы идеально подходите этой работе. Или она Вам.\n')
    if rate > len(skills)/2:
        print('Вы более, чем наполовину обладаете нужными качествами для этой вакансии.\n')
    if rate > 0:
        print('Кое-что из того, чего хочет работодатель Вы умеете.\n')
    base_of_vacancis.append([name, skills, rate])
    print('Вакансия добавлена! \n')

def allpreview (base):
    for item in base: 
        print (item)
    
def rate ():
    for vacancy in base_of_vacancis:
        rate = 0
        for skill in vacancy[1]:
            if skill in base_of_skills:
                rate += 1
        rate_to_vacancy [rate] = vacancy
    print ('Рейтинг компетенций пересчитан.\n')
    for key, value in rate_to_vacancy.items():
        print(f"Вакансия: {value[0]} \t Рейтинг: {key} ")



def wokring ():
    while True:
        choise = input("Введите команду \n* или попросите помочь \n")
        choise = translator(choise) # TODO: translator
        match (choise):
            case '/start':
                print ('\n \t \t *** Добро пожаловать! ***')
                load()
            case '/stop':
                yes = 'давайугуагаможнонаверноехзмбyesyeah'
                request = input("Сохранить сеанс перед выходом?\n")
                if request.lower() in yes:
                    save()
                print ('До новых встреч!')
                break
            case '/help':
                print_help()
            case '/addvac':
                add_vacancy()
            case '/addskill':
                add_skill()
            case '/allvac':
                allpreview(base_of_vacancis)
                # print ('раздел в разработке')
                # TODO: function to print all vacancies
            case '/allskills':
                allpreview(base_of_skills)
                # print ('раздел в разработке')
                # TODO: function to print all skills
            case '/rate':
                rate()

wokring()
