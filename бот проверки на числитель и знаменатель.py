import telebot
import datetime

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Проверить день')
    bot.send_message(message.chat.id, 'Привет, вы желаете проверить сегодняшний день недели на числитель и знаменатель?', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def check_day(message):
    if message.text == 'Проверить день':
        an = ['Числитель','Знаменатель']
        _,week_number,_ = datetime.datetime.now().isocalendar()
        result = an[week_number%2]
        bot.send_message(message.chat.id, f'Сегодня {result}')

bot.polling(none_stop=True)
