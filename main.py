import telebot
import Config
import os
Token = os.environ["TOKEN"]
bot = telebot.TeleBot(Token)
@bot.message_handler(content_types=["text", "photo"])


def get_text_messages(message):
 if message.content_type == "photo":

  bot.send_message(message.from_user.id,"Обрабатываю запрос, пару секунд")
  id = message.photo[-1].file_id
  file_info = bot.get_file(id)
  URL = f'http://api.telegram.org/file/bot{Token}/{file_info.file_path}'
  bot.send_message(message.from_user.id, Config.Predict(URL))

 elif message.content_type == "text":
  bot.send_message(message.from_user.id, "Я тебя не понимаю. Скинь фото для распознавания")

bot.infinity_polling()