TOKEN = ""

import telebot

lessons = {"понедельник": "ПРОЕКТИРОВАНИЕ АГРЕГАТОВ ТЕХНИЧЕСКИХ КОМПЛЕКСОВ, \nСАПР СТАРТОВЫХ КОМПЛЕКСОВ, \nПРОЕКТ.АГРЕГ.ТЕХН.КОМПЛ.", "вторник": "СТАБИЛИЗАЦИЯ МАШИН, \nМАТЕМАТ.МОДЕЛИРОВАНИЕ ФУНК.РАКЕТ.ТЕХНИКИ, \nПОДРЕССОРИВАНИЕ СПЕЦМАШИН", "среда": "МАТЕМАТ. МОДЕЛИРОВАНИЕ, \nЭЛЕКТРО- И ГИДРООБОРУДОВАНИЕ, \nКОЛЕСНЫЕ И ГУСЕНИЧНЫЕ МАШИНЫ", "четверг": "ИСПЫТАНИЕ И НАДЕЖНОСТЬСИСТЕМ, \nСПЕЦГЛАВЫ  МАТЕМАТИКИ, \nИСПЫТАНИЕ И НАДЕЖНОСТЬ СИСТЕМ", "пятница": "ЭФФЕКТИВН.,НАДЕЖНОСТЬ И ИСПЫТАНИЯ МАШИН, \nТЕХНОЛОГИЯ ПРОИЗВОДСТВА АРТСИСТЕМ, \nСИСТЕМОТЕХНИЧЕСКОЕ ПРОЕКТИРОВАНИЕ"}

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Приветствую, что узнать расписание, введите названия дня недели на русском")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text.lower() in lessons.keys():
		bot.reply_to(message, lessons[message.text.lower()])
	else:
		bot.reply_to(message, "Пожалуйста проверьте орфографию, и попробуйте снова. Для помощи введите '/help'")

bot.infinity_polling()
