import telebot
import json

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

user = 0
dialog = 0
skills = []

#@bot.message_handler(content_types=['text'])
def output_message(message, say):
    global user
    bot.send_message(message.chat.id, say)
    user=message.from_user.id
    print(f"user={message.from_user.id}")

def input_message(message): 
    global dialog
    dialog = 1
    return message.text

@bot.message_handler(func=lambda message: True, content_types=['text', 'sticker'])
def understand (message):
    global dialog
    global skills
    text = message.text
    print(text)
    output = 'вводите пока не скажете стоп'
    listen = ''
    if dialog != 0:
        if "навык" in text.lower():
            output_message(message, output)
            dialog = 2
            listen = input_message(message)
        elif text.lower() != 'стоп' and dialog == 1:
            print (listen)
            skills.append(listen)
            dialog = 2
        elif (text.lower() == 'стоп'): 
            dialog = 0
            output_message(message, 'вы сказали стоп')
#    bot.send_message(message.chat.id, output)
    else:
        print(skills)


bot.polling()