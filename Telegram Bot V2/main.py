import telebot
from telebot import types
import openpyxl


BOT_TOKEN = "5182232201:AAGGR8KQY15ySH9Iz4urgmQ8G-PAArgAlww"
admin_id = 437819952

bot = telebot.TeleBot(BOT_TOKEN)#Начало бота
bot.send_message(admin_id, 'Бот активен! V 2.0.0')
print('The bot is active! V 2.0.0')
print('The author of the code : Nikita Bulgak "Forbidden Peace" company  ')



bot.polling()