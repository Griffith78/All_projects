import telebot#импорт библиотеки на которой будет написан функционла бота

from telebot import types#импортируем типы для создания кнопок
from telebot.types import ReplyKeyboardMarkup, KeyboardButton#импортирование непосредственно кнопок

bot = telebot.TeleBot("7479976997:AAGLEFrRLE9gQy8udd-SoZYN8saKhOswx7o")#объект с API бота и которому мы будем обращаться по ходу программы для создания функционала

@bot.message_handler(commands = ["start"])#создаем обработку для команды start
def start(message):
    markup = types.InlineKeyboardMarkup()#создаем объект в который будем записывать все кнопки около сообщения и выводить вместе с текстом
    btn1 = types.InlineKeyboardButton("Open site", url="google.com")#первая кнопка которая будет открывать страницу гугла. В URL указываем какую страницу будем открывать
    btn2 = types.InlineKeyboardButton("Delete message", callback_data="delete")#создаем функцию удаления последнего сообщения пользователя. В Callback_data указываем какая функция будет выполняться при нажатии кнопки
    markup.row(btn1, btn2)#записываем эти две кнопки как строка в объект markup.По умолчания под 1 объект будет выделяться целая строка
    markup.add(types.InlineKeyboardButton("Open site",url="google.com")) #создаем объект в который будем записывать все кнопки и выводить вместе с текстом
    markup.add(types.InlineKeyboardButton("Delete picture", callback_data="delete")) #первая кнопка которая будет открывать страницу гугла. В URL указываем какую страницу будем открывать
    markup.add(types.InlineKeyboardButton("Edit text", callback_data="edit"))  #кнопка которая будет исправлять нынешнее сообщение бота
    bot.send_message(message.chat.id,f"Hello,user {message.from_user.first_name} {message.from_user.last_name}",reply_markup = markup )#отправляем сообщение о приветствии обращаясь к личным данным и передаем объект markup для вывода кнопок вместе с сообщением

@bot.callback_query_handler(func = lambda callback: True)#обработаем нажатия кнопок, а точнее callback которые мы вызываем при нажатии. Обязательно передать func = lambda callback: True
def callback_message(callback):#передаем 1 параметр
    if callback.data == "delete":#если пользователь нажал на кнопку за которой закреплена функция delete
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)#Вызываем функцию удаления которая удаляет не полсднее сообщения а предпоследнее а то есть сообщение пользоватлея
    if callback.data == "edit":#Если же пользователь нажал на другую кнопку тогда
        bot.edit_message_text("Text was edit", callback.message.chat.id, callback.message.message_id)#мы изменям сообщение бота на Text was edit

@bot.message_handler(commands = ["show"])#будем обробатывать вызов команды show
def show(message):
    markup = ReplyKeyboardMarkup()  #будем делать кнопки около клавиатуры пользователя по тому же методу
    markup.add(KeyboardButton("Open site"))#в эти кнопки нельзя передавать не url не callbaxck так что просто указываем текст
    markup.add(KeyboardButton("Delete picture")) #
    markup.add(KeyboardButton("Edit Text"))  #
    bot.send_message(message.chat.id,"Choose the button ",reply_markup=markup)  #будем выводит эти кнопки с этим сообщением
    bot.register_next_step_handler(message,on_click)# так как мы не можем передавать какой либо функционал будем вызывать указаную функцию которая исправит это с помощью данного метода

def on_click(message):#Так как при нажатии определенной кнопки пользователь отправляет текст который на ней написан мы будем отталкиваться от этого и отслеживать нажатия
    if message.text == "Open site":#если пользователь нажал на кнопку open sitе
        bot.delete_message(message.chat.id,message.message_id)#тогда мы сразу же удаляем сообщение отправленное пользователем чтобы не захламлять чат
        bot.send_message(message.chat.id, "Site is Open")#и выводим Site is open. C остальными кнопками делаем так же

    if message.text == "Delete picture":#
        bot.send_message(message.chat.id, "Picture Deleted") #

    if message.text == "Edit Text":#
          bot.send_message(message.chat.id, "Text edited")#

bot.polling(none_stop = True)