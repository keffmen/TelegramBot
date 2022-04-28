
import telebot
from telebot import types

BOT_TOKEN = "5182232201:AAGGR8KQY15ySH9Iz4urgmQ8G-PAArgAlww"
admin_id = 437819952
user_id = [437819952,0]
wat_id = [0,0]


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    peson = types.KeyboardButton('Для Персонала')
    userid = types.KeyboardButton('Мой id')
    website = types.KeyboardButton('Сайт')
    price = types.KeyboardButton('Скидки')
    markup.add(website, userid, peson, price)
    text = f'Приветствую, <b>{message.from_user.first_name} {message.from_user.last_name}! Выбирите категорию :</b> '
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == "Сайт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://obnovi-oboi.ru/"))
        bot.send_message(message.chat.id,"Сайт находиться в тестовом режиме" ,reply_markup=markup)
    elif message.text == "Для Персонала":
        if message.from_user.id in user_id:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            poisk = types.KeyboardButton('Найти товар')
            news = types.KeyboardButton('Новости')
            back = types.KeyboardButton('Назад')
            markup.add(news, poisk, back)
            text = f'Приветствую, Вы Авторизовались как прадовец-консультант <b>{message.from_user.first_name} {message.from_user.last_name}! Выбирите категорию :</b> '
            bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            regis = types.KeyboardButton('Отправить запрос')
            markup.add(regis,back)
            bot.send_message(message.chat.id, 'Вы не зарегистрированы! Пройти авторизацию у менеджера?', reply_markup=markup)

    elif message.text == "Найти товар":
        if message.from_user.id in user_id:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            pol = types.KeyboardButton('Напольное покрытие')
            keramika = types.KeyboardButton('Керамика')
            back = types.KeyboardButton('Назад')
            markup.add(pol, keramika, back)
            bot.send_message(message.chat.id, "Какую категорию мы смотрим ? ", reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            regis = types.KeyboardButton('Отправить запрос')
            markup.add(regis, back)
            bot.send_message(message.chat.id, 'Вы не зарегистрированы! Пройти авторизацию у менеджера?',reply_markup=markup)
    elif message.text == "Мой id":
        bot.send_message(message.chat.id, f"Ваш id : <u>{message.chat.id}</u>", parse_mode='html')
    elif message.text == "Напольное покрытие":
            bot.send_message(message.chat.id, " В разработке ")
    elif message.text == "Керамика":
            bot.send_message(message.chat.id, " В разработке ")
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        peson = types.KeyboardButton('Для Персонала')
        userid = types.KeyboardButton('Мой id')
        website = types.KeyboardButton('Сайт')
        price = types.KeyboardButton('Скидки')
        markup.add(website, userid, peson, price)
        text = "Вы вернулись )"
        bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)
    elif message.text == "Скидки":
        bot.send_message(message.chat.id, "Мы их сами ждем")
    elif message.text == "Новости":
        bot.send_message(message.chat.id, "Новостей от руководства нет!")
    elif message.text == "Отправить запрос":
        if message.from_user.id in user_id:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            poisk = types.KeyboardButton('Найти товар')
            news = types.KeyboardButton('Новости')
            back = types.KeyboardButton('Назад')
            markup.add(news, poisk, back)
            text = f'Приветствую, Вы Авторизовались как прадовец-консультант <b>{message.from_user.first_name} {message.from_user.last_name}! Выбирите категорию :</b> '
            bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            yes = types.KeyboardButton("Разрешить")
            no = types.KeyboardButton("Отменить")
            markup.add(yes, no)
            wat_id.insert(1, message.chat.id)
            msg = bot.send_message(admin_id, f"Пользователь просит авторизации : {message.chat.id}   {message.from_user.first_name} {message.from_user.last_name}", parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(msg,user_reg)

def user_reg(message):
    if message.text == "Разрешить":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        poisk = types.KeyboardButton('Найти товар')
        news = types.KeyboardButton('Новости')
        back = types.KeyboardButton('Назад')
        markup.add(news, poisk, back)
        text = f'Приветствую, Вы Авторизовались как <b>прадовец-консультант !</b> Выбирите категорию : '
        bot.send_message(wat_id[1], text, parse_mode='html', reply_markup=markup)
        bot.send_message(admin_id, "Зарегистрированно", reply_markup=markup)
        user_id.insert(1,wat_id[1])


    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        peson = types.KeyboardButton('Для Персонала')
        userid = types.KeyboardButton('Мой id')
        website = types.KeyboardButton('Сайт')
        price = types.KeyboardButton('Скидки')
        markup.add(website, userid, peson, price)
        bot.send_message(wat_id[1], "В доступе отказано", reply_markup=markup)
        bot.send_message(admin_id, "В доступе отказано", reply_markup=markup)




bot.polling()
