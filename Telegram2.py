import telepot
import json
from Primario import PrimarioBot

with open('token.json') as jsonFile:
    token = json.load(jsonFile)

telegram = telepot.Bot(token)

bot = PrimarioBot("Primario")

def receiveMsg(msg):
    phrase = bot.Ouvir(phrase=msg['text'])
    response = bot.Pensar(phrase)
    bot.Falar(response)
    msgType, chatType, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, response)

telegram.message_loop(receiveMsg)

while True:
    pass