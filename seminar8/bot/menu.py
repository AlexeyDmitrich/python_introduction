import languageModule as lm
import functions as func

def wokring (choise=''):
    while True:
#        choise = input("\n Введите команду \n (ну или попросите помочь) \n")
        choise = lm.translator(choise) # TODO: translator
        match (choise):
            case '/stop':
                yes = 'сохранитьдавайугуагаможнонаверноехзмбyesyeahsave'
                request = input("Сохранить сеанс перед выходом?\n")
                if request.lower() in yes:
                    func.save()
                print ('Не забывайте добавлять новые навыки! \n До новых встреч!')
                break
            case '/help':
                func.print_help()
            case '/addvac':
                func.add_vacancy()
            case '/addskill':
                func.add_skill()
            case '/allvac':
                func.allpreview(func.base_of_vacancis)
            case '/allskill':
                func.allpreview(func.base_of_skills)
            case '/rate':
                func.rate()