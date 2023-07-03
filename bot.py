import telebot
import sqlite3
from kernel import migrations
import config

db = sqlite3.connect("database.db")
cursor = db.cursor()

migrations.migrate(db, cursor)

bot = telebot.TeleBot(config.tg_bot_api_key)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.reply_to(message, """\
Hello motherfucker
""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
