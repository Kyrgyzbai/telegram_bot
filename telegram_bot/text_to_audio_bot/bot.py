import telebot
import pyttsx3
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
        audio_engine = pyttsx3.init()
        # создаем имя файла mp3 с помощью временной метки
        filename = str(calendar.timegm(time.gmtime())) + '.mp3'

        # преобразуем текст в аудио
        # и отправляем в папку /home/neo/Downloads/audios/*.mp3
        audio_engine.save_to_file(
            text,
            '/home/neo/Downloads/audios/' + filename
        )
        audio_engine.setProperty('rate', 20)
        # запуск аудио движка для сохранения
        audio_engine.runAndWait()

        # отправляем клиенту сообщение
        bot.send_message(chat_id, 'Ваше аудио: ')
        audio_file = open('/home/neo/Downloads/audios/' + filename, 'rb')
        bot.send_audio(chat_id, audio_file)

print('Бот работает...')
bot.polling()