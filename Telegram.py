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
""" 
def handle(msg):
    pprint(msg)
MessageLoop(bot, handle).run_as_thread()
bot.sendMessage('Here is a ID number', 'Hey!')
"""
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])

MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10) 