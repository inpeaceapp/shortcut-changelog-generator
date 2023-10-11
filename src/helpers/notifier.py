import os
import helpers.settings as settings
from telegram import Bot
from telegram.utils.helpers import escape_markdown

def telegram(message):
    bot = Bot(settings.telegram_bot_token)

    if settings.telegram_title is not None:
        message = '*' + escape_markdown(settings.telegram_title) + '*' + '\n\n' + message

    if len(message) > 4096:
        for x in range(0, len(message), 4096):
            bot.send_message(chat_id=settings.telegram_chat_id, text=message[x:x+4096], parse_mode='MarkdownV2')
    else:
        bot.send_message(chat_id=settings.telegram_chat_id, text=message, parse_mode='MarkdownV2')