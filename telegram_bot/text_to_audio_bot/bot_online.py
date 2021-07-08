import telebot
import gtts
import calendar
import time

bot = telebot.TeleBot('1631527655:AAG8mmpedeFTTzB5adRATRVN4xB4ZoaqIoU')

@bot.message_handler(content_types='text')
def get_message(message):
    message_splitted = message.text.lower().split('=')

    command = message_splitted[0].strip()
    text = message_splitted[1].strip()
    chat_id = message.chat.id

    if command == 'скажи':
        # создаем имя файла mp3 с помощью временной метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'

        audio = gtts.gTTS(text, lang='ru')
        audio.save('/home/neo/Downloads/audios/' + filename)

        bot.send_message(chat_id, 'Ваше аудио готово щас')
        bot.send_message(chat_id, 'Сейчас отправлю)))')

        audio_file = open('/home/neo/Downloads/audios/' + filename, 'rb')
        bot.send_audio(chat_id, audio_file)
    elif command == 'tell':
        pass


print('Бот работает...')
bot.polling()