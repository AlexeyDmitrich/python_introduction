import telebot
import menu
import json
import requests

try:
    with open ('token.json', 'r', encoding='UTF-8') as tk:
        API_TOKEN = (json.load(tk))[0]
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

@bot.message_handler(commands=['start'])
def start_message(message):
    global user
    global users
    global chat
    bot.send_message(message.chat.id, "добро пожаловать!")
    users.append(message.from_user.id)
    user=message.from_user.id
    print(f"user={message.from_user.id}")
#    print(message)
#    chat=message.from_chat.id
#    print(f'chat={message.from_chat.id}')

@bot.message_handler(func=lambda message: True, content_types=['text', 'sticker'])
def understand (message):
    text = message.text
    menu.working(text)


bot.polling()