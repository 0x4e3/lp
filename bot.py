# coding=utf-8
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import InvalidToken


TELEGRAM_API_TOKEN = '374823991:AAEpegnagW8yHNzDC1J52wR1DJ4A2fBcoxE'


def greet_user(bot, update):
    user_info = update.message.to_dict().get('from', {})
    if user_info:
        greeting = "Hi, {first_name} {last_name}! Let's chat together!". \
            format(**user_info)
    else:
        greeting = 'Давай общаться!'
    bot.sendMessage(update.message.chat_id, text=greeting)


def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)


def show_error(bot, update, error):
    print(error)


def main():
    print('Starting poller...')

    try:
        updater = Updater(TELEGRAM_API_TOKEN)
    except InvalidToken:
        print('Error: Something went wrong with your token!')
        sys.exit(1)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)

    print('Poller has been started, now polling till the end of time...')
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
