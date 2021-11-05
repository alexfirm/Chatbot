import telepot, json, time
from Primario import Test
from telepot.loop import MessageLoop

with open("Token.json") as jsonFile:
  token = json.load(jsonFile)

telegram = telepot.Bot(token)
bot = Test("Memoria")

def receiveMsg(msg):
  frase = bot.listen(phrase=msg['text'])
  resposta = bot.think(frase)
  bot.speak(resposta)
  
  content_type, chat_type, chat_id = telepot.glance(msg)
  telegram.sendMessage(chat_id, resposta)

MessageLoop(telegram, receiveMsg).run_as_thread()

while 1: #1 significa True, 0 significa False
    time.sleep(10) 