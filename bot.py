#Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token='527338094:AAHj23l2294N1ijDhMqr9HtQKJ8ygTZzlfI')
#Токен API к Telegram
dispatcher = updater.dispatcher
#Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Приветствую. Я Бот-Один. Мой создатель Данил Кущ. Я очень люблю общатсья с людьми. Спрашивай меня о чем-то хорошем и не обижай, тогда я стану лучше и ты тоже). ')
def textMessage(bot, update):
    request = apiai.ApiAI('30c97e9e76b7432d85679f2969aa0912').text_request() #Токен API к Dialogflov
    request.lang = 'ru' #На каком языке будет послан запрос
    request.session_id = 'BatlabAIBot' #ID сессии диалога (для обучения бота в дальнейшем)
    request.query = update.message.text #осылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] #Разбираем JSON и вытаскиваем ответ
    #Если есть ответ - посылаем юзеру, нет ответа - бот его не понял
    if response:
        bot.send_message(chat_id = update.message.chat_id, text = response)
    else:
        bot.send-send_message(chat_id = update.message.chat_id, text = 'Я вас не понял.')
#Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
#Добавляем хендлеры в диспатчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
#Начинаем поиск обновлений
updater.start_polling(clean=True)
#Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
