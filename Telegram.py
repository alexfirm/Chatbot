import telepot
import json
from pprint import pprint
from telepot.loop import MessageLoop
import time

with open("Token.json") as jsonFile:
  token = json.load(jsonFile)

bot = telepot.Bot(token)

#print(bot.getMe())
#response = bot.getUpdates()
#print(response)
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        #bot.sendMessage(chat_id, msg['text'])
        bot.sendMessage(chat_id, 'Hi')

MessageLoop(bot, handle).run_as_thread()
print('Executando ...')

while 1: #1 significa True, 0 significa False
    time.sleep(10) 