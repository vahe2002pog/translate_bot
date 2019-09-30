import config
import urllib.request
import urllib.parse
import json
import telebot

bot = telebot.TeleBot(config.token) 

@bot.message_handler(content_types=["text"])
def send_echo(message):
    query = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=" + config.key + '&text=' + urllib.parse.quote(message.text) + '&lang=ru&format=plain'
    req = urllib.request.urlopen(query).read()
    text = json.loads(req)
    bot.send_message(message.chat.id, text['text'])

if __name__ == '__main__':
    bot.polling(none_stop=True)