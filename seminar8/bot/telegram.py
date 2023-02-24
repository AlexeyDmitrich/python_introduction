import telebot
import menu
import json
import functions as func
import requests
import languageModule

try:
    with open ('token.json', 'r', encoding='UTF-8') as tk:
        API_TOKEN = (json.load(tk))
except:
    print('Не найден токен')
    new_token = input("Введите новый API-токен")
    try:
        with open ('token.json', 'w', encoding='UTF-8') as tk:
            tk.write(json.dumps(new_token, ensure_ascii=False))
    except:
        print("Не удалось привязать новый токен")
bot = telebot.TeleBot(API_TOKEN)

users = [] # нужен какой-то учёт пользователей
user = ''
load_status = False
dialog = 0 
# 0 - диалог не начат
# 1 - ожидание ввода
# 2 - удержание
replic = ''

@bot.message_handler(commands=['start'])
def start_message(message):
    global user
    global users
    global load_status
    bot.send_message(message.chat.id, "добро пожаловать!")
    users.append(message.from_user.id)
    user=message.from_user.id
    output = func.load(user)
    load_status = True
    print(f"user={message.from_user.id}")
#    print(message)
    bot.send_message(message.chat.id, output)
    
#    chat=message.from_chat.id
#    print(f'chat={message.from_chat.id}')

# @bot.message_handler(func=lambda message: True, content_types=['text', 'sticker'])
# def understand (message):
#     text = message.text
#     output = str(menu.working(text))
#     print(text)
#     print(output)
#     bot.send_message(message.chat.id, output)

@bot.message_handler(func=lambda message: True, content_types=['text', 'sticker'])
def understand (message):
    global load_status
    global dialog
    if load_status == False:
        user=message.from_user.id
        func.load(user)
    
    text = message.text
    print(text)
    output = ''
    translate = ''
    if dialog == 0:
        translate = languageModule.translator(text)     # переводим речь в команду для бота
        # если подходящей команды не нашлось - возвращаем фразу в неизменном виде
        
        output = str(menu.working(message.from_user.id, translate)) # команда уходит в меню
    if output != translate: # если команда что-то вернула, кроме самой себя
        print(output)       # (для команд, которые есть в меню)
    else:   # если команды не нашлось
            # сюда нужно поместить функции для добавления скиллов
        if output == '/addskill':
            dialog = 1
        #    bot.send_message(message.chat.id, 'Введите навык \nесли новых навыков больше нет, скажите хватит \n' )
        if dialog == 1:
            wait_answer(user, 'Введите навык \nесли новых навыков больше нет, скажите хватит \n')
            if text.lower == 'хватит':
                dialog = 0
                return
            else:
                bot.send_message(user, f'{output} вы ввели: {text}')
                dialog = 2
                
        # для добавления вакансий
        # AI для поддержания диалога
                
        
    bot.send_message(message.chat.id, output)

def wait_answer (user, quest):
    global dialog
    if dialog == 1:
        bot.send_message(user, quest)
        user_input = bot.message_handler(func=lambda message: True, content_types=['text', 'sticker'])
        
        print (user_input)
        return user_input
    if dialog == 2: 
        return
        

bot.polling()
