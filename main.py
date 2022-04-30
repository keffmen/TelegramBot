
import telebot
from telebot import types
import openpyxl



BOT_TOKEN = "5182232201:AAGGR8KQY15ySH9Iz4urgmQ8G-PAArgAlww"
admin_id = 437819952
wat_id = []


bot = telebot.TeleBot(BOT_TOKEN)
bot.send_message(admin_id, 'Бот активен !')


@bot.message_handler(commands = ['start'])
def start(message):
    array = open("newuserid.txt", "r").readlines()
    arrayid = message.chat.id
    a = False
    for i in array:
        if int(i) == arrayid:
            print(f"ravno {i} - {arrayid}")
            a = True
            break
    if str(a) == "False" :
        with open("newuserid.txt", 'a+') as newuserid:
            print(message.chat.id, file=newuserid)
            array.clear()
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            peson = types.KeyboardButton('Для Персонала')
            userid = types.KeyboardButton('Мой id')
            website = types.KeyboardButton('Сайт')
            price = types.KeyboardButton('Скидки')
            dostavka = types.KeyboardButton('Узнать где мой товар ?!')
            markup.add(website, userid, peson, price, dostavka)
            bot.send_message(message.chat.id, f"Привет ты впервые у нас , и я записал твой id : {arrayid}. Ты можешь выбрать категорию ", parse_mode='html', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        peson = types.KeyboardButton('Для Персонала')
        userid = types.KeyboardButton('Мой id')
        website = types.KeyboardButton('Сайт')
        price = types.KeyboardButton('Скидки')
        dostavka = types.KeyboardButton('Узнать где мой товар ?!')
        markup.add(website, userid, peson, price, dostavka)
        text = f'Приветствую, <b>{message.from_user.first_name} {message.from_user.last_name}! Выбирите категорию :</b> '
        bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == "Сайт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://obnovi-oboi.ru/"))
        bot.send_message(message.chat.id,"Сайт находиться в тестовом режиме" ,reply_markup=markup)

    elif message.text == "Узнать где мой товар ?!":
            msg = bot.send_message(message.chat.id, "<b><u>Укажите номер телефона через 8</u></b> на кого была зарегистрирована заявка", parse_mode='html')
            bot.register_next_step_handler(msg, result_delivery)

    elif message.text == "Для Персонала":
        array = open("Adminid.txt", "r").readlines()
        arrayid = message.chat.id
        a = False
        for i in array:
         if int(i) == arrayid:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            poisk = types.KeyboardButton('Найти товар')
            news = types.KeyboardButton('Новости')
            back = types.KeyboardButton('Назад')
            mass_message = types.KeyboardButton('Рассылка сообщений')
            markup.add(news, poisk, back, mass_message)
            text = f'Приветствую, Вы Авторизовались как прадовец-консультант <b>{message.from_user.first_name} {message.from_user.last_name}! Выбирите категорию :</b> '
            bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)
            a = True
            break
        if str(a) == "False":
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            regis = types.KeyboardButton('Отправить запрос')
            markup.add(regis,back)
            bot.send_message(message.chat.id, 'Вы не зарегистрированы! Пройти авторизацию у менеджера?', reply_markup=markup)

    elif message.text == "Найти товар":
        array = open("Adminid.txt", "r").readlines()
        arrayid = message.chat.id
        a = False
        for i in array:
            if int(i) == arrayid:
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                pol = types.KeyboardButton('Напольное покрытие')
                keramika = types.KeyboardButton('Керамика')
                back = types.KeyboardButton('Назад')
                markup.add(pol, keramika, back)
                bot.send_message(message.chat.id, "Какую категорию мы смотрим ? ", reply_markup=markup)
                a = True
                break
        if str(a) == "False":
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
            msg = bot.send_message(message.chat.id, "Введите артикул :")
            bot.register_next_step_handler(msg, art_result)
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        peson = types.KeyboardButton('Для Персонала')
        userid = types.KeyboardButton('Мой id')
        website = types.KeyboardButton('Сайт')
        price = types.KeyboardButton('Скидки')
        dostavka = types.KeyboardButton('Узнать где мой товар ?!')
        markup.add(website, userid, peson, price, dostavka)
        text = "Вы вернулись )"
        bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)
    elif message.text == "Скидки":
        bot.send_message(message.chat.id, "Мы их сами ждем")
    elif message.text == "Новости":
        bot.send_message(message.chat.id, "Новостей от руководства нет!")
    elif message.text == "Отправить запрос":
        array = open("Adminid.txt", "r").readlines()
        arrayid = message.chat.id
        for i in array:
            if int(i) == arrayid:
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                poisk = types.KeyboardButton('Найти товар')
                news = types.KeyboardButton('Новости')
                back = types.KeyboardButton('Назад')
                mass_message = types.KeyboardButton('Рассылка сообщений')
                markup.add(news, poisk, back, mass_message)
                text = f'Приветствую, Вы Авторизовались как прадовец-консультант <b>{message.from_user.first_name} {message.from_user.last_name}! Выбирите категорию :</b> '
                bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)

        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        yes = types.KeyboardButton("Разрешить")
        no = types.KeyboardButton("Отменить")
        markup.add(yes, no)
        wat_id.insert(0, message.chat.id)
        msg = bot.send_message(admin_id, f"Пользователь просит авторизации : {message.chat.id}   {message.from_user.first_name} {message.from_user.last_name}", parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(msg,user_reg)

def art_result(message):
        art = message.text
        xl = openpyxl.open(filename='ПРАЙС_ВОГ-розница.xlsx')
        xl.active = 0
        sheet = xl.active
        a = False
        for i in range(1, len(sheet['B']) + 1):
            if art == sheet['B' + str(i)].value:
               bot.send_message(message.chat.id, f"Это плитка : {sheet['A' + str(i)].value} ")
               bot.send_message(message.chat.id, f"Цена этой плитки : {sheet['G' + str(i)].value} за {sheet['H' + str(i)].value} ")
        if str(a) == "False":
            if message.text == "Назад":
                markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                peson = types.KeyboardButton('Для Персонала')
                userid = types.KeyboardButton('Мой id')
                website = types.KeyboardButton('Сайт')
                price = types.KeyboardButton('Скидки')
                dostavka = types.KeyboardButton('Узнать где мой товар ?!')
                markup.add(website, userid, peson, price, dostavka)
                text = "Вы вернулись )"
                bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=markup)
                quit()
            msg = bot.send_message(message.chat.id, f"Введите еще ! Я не чего не нашел")
            bot.register_next_step_handler(msg, art_result)

def result_delivery (message):
   phone = message.text
   bot.send_message(message.chat.id, f"По указаному номеру телефона <b><u>{phone}</u></b> не чего не найдено!", parse_mode='html')

def user_reg(message):
    if message.text == "Разрешить":
        with open("Adminid.txt", 'a+') as Admonid:
         print(wat_id[0], file=Admonid)
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        poisk = types.KeyboardButton('Найти товар')
        news = types.KeyboardButton('Новости')
        back = types.KeyboardButton('Назад')
        mass_message = types.KeyboardButton('Рассылка сообщений')
        markup.add(news, poisk, back, mass_message)
        text = f'Приветствую, Вы Авторизовались как <b>прадовец-консультант !</b> Выбирите категорию : '
        bot.send_message(wat_id[0], text, parse_mode='html', reply_markup=markup)
        bot.send_message(admin_id, "Зарегистрированно", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        peson = types.KeyboardButton('Для Персонала')
        userid = types.KeyboardButton('Мой id')
        website = types.KeyboardButton('Сайт')
        price = types.KeyboardButton('Скидки')
        dostavka = types.KeyboardButton('Узнать где мой товар ?!')
        markup.add(website, userid, peson, price, dostavka)
        bot.send_message(wat_id[0], "В доступе отказано", reply_markup=markup)
        bot.send_message(admin_id, "В доступе отказано", reply_markup=markup)



bot.polling()
