import telebot
from telebot import types
import random 

bot = telebot.TeleBot('6054612632:AAGyqzOa6xlc6juC1AuoaLeXFWG5HuhKcSc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    random_button = types.InlineKeyboardButton('Рандом', callback_data='random')
    website_button = types.InlineKeyboardButton('Веб-сайт', url='https://example.com')
    markup.add(random_button, website_button)
    
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'random':
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, 
                                  text=f"Случайное число: {random.randint(1, 100)}")

bot.polling(non_stop=True)
