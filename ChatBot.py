import logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Jarvis')
#bot.set_trainer(ListTrainer)
trainer=ListTrainer(bot)
#trainer.train(data)

while True:
    message = input('You:')
    if message.upper().strip() != 'BYE':
        reply = bot.get_response(message)
        print('ChatBot:',reply)
    if message.upper().strip() == 'BYE':
        print('ChatBot:Bye..')
        break
