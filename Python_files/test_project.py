import telebot
import sqlite3
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('7863780400:AAHjL1GRqD19PKAsV-Sefy20doMrls0z6RY')

word = ''

@bot.message_handler(commands = ['start'])
def start(message):
    conn = sqlite3.connect('Test.sql')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dictionaries (id INTEGER PRIMARY KEY AUTOINCREMENT,word varchar(50), translation varchar(50) )")
    conn.commit()
    cur.close()
    conn.close()

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Add', callback_data = 'Add'))
    markup.add(InlineKeyboardButton('Find', callback_data = 'Find'))
    markup.add(InlineKeyboardButton('Delete', callback_data = 'Delete'))
    markup.add(InlineKeyboardButton('Print', callback_data = 'Print'))
    bot.send_message(message.chat.id,'Hello,my friend. It is dictionary',reply_markup = markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Cancel', callback_data = 'Cancel'))
    if callback.data == 'Add':
       bot.send_message(callback.message.chat.id,'Good. Write word')
       bot.register_next_step_handler(callback.message,register_word)

    if callback.data == 'Find':
        bot.send_message(callback.message.chat.id,'write word')
        bot.register_next_step_handler(callback.message,find_word)

    if callback.data == 'Delete':
        print_dict(callback.message)
        time.sleep(0.5)
        bot.send_message(callback.message.chat.id,'Here''s the whole dictionary. Specify the ID of the word you want to delete ')
        bot.register_next_step_handler(callback.message,delete)

    if callback.data == 'Add_another_word':
        bot.send_message(callback.message.chat.id, 'Good. Write word')
        bot.register_next_step_handler(callback.message, register_word)

    if callback.data == 'Print':
        print_dict(callback.message)

    if callback.data == 'Cancel':
        return

def delete(message):
    word_id = message.text.strip()
    conn = sqlite3.connect('Test.sql')
    cur = conn.cursor()
    cur.execute("DELETE FROM dictionaries WHERE id = '%s'" %(word_id))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id,'The word has been successfully deleted ')

def print_dict(message):
    conn = sqlite3.connect('Test.sql')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionaries")
    query = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    all_words = ''
    for i in query:
        all_words += f'•ID: {i[0]} | Word: {i[1]} | Translation: {i[2]} \n'
    bot.send_message(message.chat.id ,all_words)

def find_word(message):
    try:
        search_word = message.text.strip()
        conn = sqlite3.connect('Test.sql')
        cur = conn.cursor()
        cur.execute("SELECT * FROM dictionaries WHERE word = '%s'" %(search_word))
        query_result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        result = f'ID: {query_result[0]} Word: {query_result[1]} Translation: {query_result[2]}'
        bot.send_message(message.chat.id,result)
    except TypeError:
        bot.send_message(message.chat.id,'The word was not found or the input was incorrect ')

def register_word(message):
    global word
    word = message.text.strip()
    bot.send_message(message.chat.id,'Now,write translation')
    bot.register_next_step_handler(message,register_translation )

def register_translation(message):
    global word
    translation =  message.text.strip()
    conn = sqlite3.connect('Test.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO dictionaries(word,translation) VALUES ('%s','%s' )" %(word,translation))
    conn.commit()
    cur.close()
    conn.close()
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Add another',callback_data = 'Add_another_word'))
    bot.send_message(message.chat.id,'Word successfully added ', reply_markup = markup)

bot.polling(none_stop = True)