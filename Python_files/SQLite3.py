import telebot
import sqlite3

from telebot import types
from telebot.types import InlineKeyboardButton#

bot = telebot.TeleBot("7479976997:AAGLEFrRLE9gQy8udd-SoZYN8saKhOswx7o")#

name = None #в будущем нам нужно будет передать имя пользователя для вывода которое будет находиться в другой функции и соответственно будет локальной. Но мы создадим уже здесь эту переменную и в будущем заполним ее

@bot.message_handler(commands = ["start"] )
def start(message):
    conn = sqlite3.connect("Test.sql")#создаем переменую в которой подключаемся к базе данных под названием Test если же программа ее не находит то создаст новую БД с таким же названием
    cur = conn.cursor()#создаем курсор через который будем обращаться к БД и инициализировать всяческие таблицы и переменные
    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,name varchar(50), pass varchar(50) )")#обращаемся к курсору и говорим чтобы он выполнил следующею команду. В ней мы говорим чтобы программа создала таблицу users в БД с полями id которое будет заполняться автоматически а то есть с каждым разом увеличиваться на 1 а также ключ id не может повторяться. Еще содержит поле name строковый тип данных который не может содержать больше 50 символов
    conn.commit()#сохраняем все изменения совершенные в таблице
    cur.close()#а затем обрываем соединение с курсором
    conn.close()#и таблицей

    bot.send_message(message.chat.id,f"Hello, dear {message.from_user.first_name}. Please, write your name")#просим пользователя вписать имя
    bot.register_next_step_handler(message,user_name)#вызываем следующею функцию

def user_name(message):#
    global name#указываем что переменная name глобальна и мы можем ее изменить в этой функции
    name = message.text.strip()#записываем введенный пользователем текст в переменную name
    bot.send_message(message.chat.id,"Great! Now, write your password")#просим ввести пароль
    bot.register_next_step_handler(message,user_password)#вызываем следующею функцию

def user_password(message):#
    password = message.text.strip()#где записываем текст введенный пользователем в пароль

    conn = sqlite3.connect("Test.sql")#
    cur = conn.cursor()#
    cur.execute(f"INSERT INTO users(name,pass) VALUES ('%s','%s' )" %(name,password))#а также добавляем эти поля в таблицу
    conn.commit()#
    cur.close()#
    conn.close()#

    markup = types.InlineKeyboardMarkup()#
    markup.add(InlineKeyboardButton("Print users", callback_data = "Users"))#
    bot.send_message(message.chat.id,"Done! I'am Register you ",reply_markup = markup)#здесь создаем и передаем кнопку которая будет выводить всех пользователей

@bot.callback_query_handler(func = lambda callback: True)#
def callback(callback):#
    conn = sqlite3.connect("Test.sql")#
    cur = conn.cursor()#
    cur.execute(f"SELECT * FROM users")#при нажатии на кнопку человеку будет выводиться все пользователи
    print = cur.fetchall()#
    cur.close()#
    conn.close()#
    users = ""#
    for i in print:#
           users += f"User name: {i[1]} User password {i[2]}\n"#

    bot.send_message(callback.message.chat.id,users)#
@bot.message_handler(commands = ["Delete"] )
def start(message):
    conn = sqlite3.connect("Test.sql")#создаем переменую в которой подключаемся к базе данных под названием Test если же программа ее не находит то создаст новую БД с таким же названием
    cur = conn.cursor()#создаем курсор через который будем обращаться к БД и инициализировать всяческие таблицы и переменные
    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,name varchar(50), pass varchar(50) )")#обращаемся к курсору и говорим чтобы он выполнил следующею команду. В ней мы говорим чтобы программа создала таблицу users в БД с полями id которое будет заполняться автоматически а то есть с каждым разом увеличиваться на 1 а также ключ id не может повторяться. Еще содержит поле name строковый тип данных который не может содержать больше 50 символов
    cur.execute("DROP TABLE users")#обращаемся к курсору и говорим чтобы он выполнил следующею команду. В ней мы говорим чтобы программа создала таблицу users в БД с полями id которое будет заполняться автоматически а то есть с каждым разом увеличиваться на 1 а также ключ id не может повторяться. Еще содержит поле name строковый тип данных который не может содержать больше 50 символов
    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,name varchar(50), pass varchar(50) )")#обращаемся к курсору и говорим чтобы он выполнил следующею команду. В ней мы говорим чтобы программа создала таблицу users в БД с полями id которое будет заполняться автоматически а то есть с каждым разом увеличиваться на 1 а также ключ id не может повторяться. Еще содержит поле name строковый тип данных который не может содержать больше 50 символов
    conn.commit()#
    cur.close()#
    conn.close()#

    bot.send_message(message.chat.id,"delete")

bot.polling(none_stop = True)#прописываем