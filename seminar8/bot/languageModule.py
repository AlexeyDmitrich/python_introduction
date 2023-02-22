def translator (users_text):
    stop = '/stopстопостановитьхватитпрекратиуйтивыходвыйтизакончитьexitquit'
    help = '''/helpmanualпомощьпомочьпомогитемануалсправка 
    что ты можешь? что ты умеешь?'''
    show = 'showviewopenпокажипоказатьпросмотретьпосмотретьвзглянутьоткрытьоткройвсесформируйвыведивывести'
    add = 'добавитьдобавьвнестивнесидополнитьсоздатьсоздай'
    addvac = '/addvacвакансиивакансиювакант' 
    addskill = '/addskillопытумениеуменияпрактикускиллынавыки'  
    rate = '/ratestatisticрейтингстатистикастатистикупроанализируй' 
    
    if str(users_text).lower() in stop:
        return '/stop'

    if str(users_text).split()[0].lower() in add:
        if str(users_text).split()[-1].lower() in addvac:
            return '/addvac'
        if str(users_text).split()[-1].lower() in addskill:
#            print(str(users_text).split()[-1])
            return '/addskill'


    if str(users_text).split()[0].lower() in show:
        if str(users_text).split()[-1].lower() in addvac:
            return '/allvac'
        if str(users_text).split()[-1].lower() in addskill:
#            print(f"{((str(users_text).split()[-1]).upper)}:")
            return '/allskill'
        if str(users_text).split()[-1].lower() in rate:
#            print(f"{(str(users_text).split()[-1].upper)}:")
            return '/rate'

    for i in range(len(list((users_text).split()))):
        # print(str(users_text).split()[i].lower())
        if str(users_text).split()[i].lower() in help:
            return '/help'


    if str(users_text).lower() in addvac:
        return '/addvac'
    if str(users_text).lower() in addskill:
        return '/addskill'
    if str(users_text).lower() in rate:
        return '/rate'
    else:
        return users_text