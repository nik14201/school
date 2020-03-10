import telebot
import config
from weather.models import Weather
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    mes = '''
'/start' - Запустить бота
'/help'  - Помощь
'/weather' - Запросить погоду
    '''
    bot.send_message(message.chat.id, str(mes))


@bot.message_handler(commands=['weather', 'Weather', 'Погода', 'погода'])
def start_message(message):
    weather = Weather.objects.all().order_by('-id')[:1][0]
    weather_mes = "'Привет, ты запросил погоду!' \n  %s,  температура %s,  %s" % (weather.city, weather.temperature, weather.wind)
    print(weather_mes)
    bot.send_message(message.chat.id, str(weather_mes))


@bot.message_handler(commands=['help'])
def start_message(message):
    mes = '''
'/start' - Запустить бота
'/help'  - Помощь
'/weather' - Запросить погоду
    '''
    bot.send_message(message.chat.id, mes)


@bot.message_handler(content_types=['text'])
def mes(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)

#RUN
bot.polling(none_stop=True, timeout=50)
