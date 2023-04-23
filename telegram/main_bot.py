import telebot
from telebot import types
from telegram.config_telegram import token


bot = telebot.TeleBot(token)
admin_buttons = ['Создать товар', 'Удалить товар', 'Блокировать Пользователя']
admins_list = [997029220]
super_admins_list = [997029220]
state_add_admins = False
make_item = 0
arg_item = []
making_item = False


@bot.message_handler(commands=['start'])
def start(message):
    all_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.from_user.id in admins_list:
        for i in admin_buttons:
            button = types.KeyboardButton(i)
            all_buttons.add(button)
    if message.from_user.id in super_admins_list:
        all_buttons.add(types.KeyboardButton('Добавить админа'))
    bot.send_message(message.chat.id, (f'Привет {message.from_user.first_name}! Меня зовут WS_Bot, я помогу'
                                       f'вам завершить покупку товара, а также сообщу вам, когда он придёт на склад'),
                     reply_markup=all_buttons)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'для того чтобы узнать когда придёт товар напишите мне /myitem')


@bot.message_handler(content_types=['text', 'photo'])
def text_message(message):
    global state_add_admins, make_item, arg_item, making_item
    if message.chat.id in admins_list and making_item:
        if make_item <= 3:
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)
            arg_item.append(downloaded_file)
        if 3 < make_item <= 5:
            arg_item.append(str(message.text))
        if make_item == 6:
            arg_item.append(str(message.foto))
        if make_item == 7:
            bot.send_message(message.chat.id, f'Вы уверены что хотите создать новый товар? Убедитесь, что все данные'
                                              f'указанны верно и в правильном порядке(main_foto, dop_foto_1,'
                                              f'dop_foto_2, dop_foto_3,name_of_item, description, cost(int).'
                                              f'Если всё указанно корректно, то напишите yes')
        if make_item == 8 and message.text.lower() == 'yes':
            pass #здесь нужно добавить все данные из списка arg_item
        make_item += 1
        if make_item == 9:
            make_item = 0
            arg_item = []
            making_item = False
    if message.chat.id in super_admins_list and state_add_admins and str(message.text).isdigit():
        admins_list.append(int(message.text))
        state_add_admins = False
        bot.send_message(message.chat.id, f'Пользователю с id: {message.text} выдан администраторский статус. Для'
                                          f'появления панели администратора ему необходимо ещё раз написать мне /start')
    if message.text == 'Создать товар' and message.chat.id in admins_list:
        bot.send_message(message.chat.id, f'Чтобы добавить товар следующими сообщениями отправляй мне данные'
                                          f'в следующем порядке: main_foto, dop_foto_1, dop_foto_2, dop_foto_3,'
                                          f'name_of_item, description, cost(int)')
        make_item = 0
        arg_item = []
        making_item = True
    if message.text == 'Удалить товар' and message.chat.id in admins_list:
        pass
    if message.text == 'Блокировать Пользователя' and message.chat.id in admins_list:
        pass
    if message.text == 'Добавить админа' and message.chat.id in super_admins_list:
        bot.send_message(message.chat.id, f'Чтобы добавить админа напиши мне его id в телеграмм следующим сообщением')
        state_add_admins = True
    state_add_admins = False



bot.infinity_polling()