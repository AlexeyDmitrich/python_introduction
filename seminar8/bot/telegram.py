import telebot
import menu
API_TOKEN = '6012033158:AAHBOz2RtYjWL4zyn6aKejHDXrsLEzVRbxs'
bot = telebot.TeleBot(API_TOKEN)

users = [] # нужен какой-то учёт пользователей

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "добро пожаловать!")
    users.append(message.from_user.id)

@bot.message_handler(func=lambda message: True, content_types=['text', 'sticker'])
def understand (message):
    text = message.text
    
bot.polling()