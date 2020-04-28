import json
import os
from bot.bot import Bot
from bot.handler import MessageHandler
from dotenv import load_dotenv
import random

load_dotenv()


def message_cb(bot, event):
    if event.text == "flip":
        coin = random.randint(1, 2)
        text = "Орел!" if coin==1 else "Решка!"
        bot.send_text(chat_id=event.from_chat, text=text)
    else:
        bot.send_text(chat_id=event.from_chat, text='Я только уменю подбрасывать монетку, напиши flip')


def main():
    bot = Bot(token=os.getenv("TOKEN"))
    bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()