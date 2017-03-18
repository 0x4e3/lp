# coding=utf-8
import sys
import re
import operator
from datetime import date
from functools import wraps

import enchant
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import InvalidToken


TELEGRAM_API_TOKEN = '374823991:AAEpegnagW8yHNzDC1J52wR1DJ4A2fBcoxE'

# TODO: Add logging
def send_reply_to_user(func):
    @wraps(func)
    def wraper(bot, update, args):
        reply_text = func(bot, update, args)
        if not reply_text and not isinstance(reply_text, str):
            print('Your handler "{}" should return some text.'.
                format(func.__name__))
            reply_text = 'Ой, у нас там что-то пошло как-то не так.'
        bot.sendMessage(update.message.chat_id, text=reply_text)
    return wraper


def greet_user(bot, update):
    user_info = update.message.from_user
    if user_info:
        greeting = "Hi, {} {}! Let's chat together!". \
            format(user_info.first_name, user_info.last_name)
    else:
        greeting = 'Давай общаться!'
    bot.sendMessage(update.message.chat_id, text=greeting)


@send_reply_to_user
def find_planet(bot, update, args):
    if not args:
        return 'Хорошо бы указать название планеты!'
    planet_name = args[0]
    planet_name = planet_name.capitalize()
    dictionary = enchant.Dict('en_US')
    if not dictionary.check(planet_name):
        return 'Название планеты должно быть на английском!'
    planets_available = [line[2] for line in ephem._libastro.builtin_planets()]
    if planet_name in planets_available:
        planet = getattr(ephem, planet_name)
        _, constellation_name = ephem. \
            constellation(planet(date.today()))
        return 'Сегодня планета в созвездии {}'. \
            format(constellation_name)
    else:
        return 'Ничего не знаю про такую планету =('


@send_reply_to_user
def count_words(bot, update, args):
    if not args:
        return 'Я не могу считать пустоту!'
    starts_with_quote = args[0].startswith('"') or args[0].startswith("'")
    ends_with_quote = args[-1].endswith('"') or args[-1].endswith("'")
    if not starts_with_quote or not ends_with_quote:
        return 'Строка всегда должна быть в кавычках!'
    return 'всего слов {:d}'.format(len(args))


@send_reply_to_user
def calculate(bot, update, args):
    if not args:
        return 'Я не могу считать пустоту!'
    expr = args[0]
    if not expr.endswith('='):
        return 'Выражение должно заканчиваться знаком "="'
    builtin_operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv}
    expr_parced = re.findall(r'\d+|[+-/*]', expr)
    if len(expr_parced) != 3:
        return 'С вашим выражением не так, BTW, я знаю только ' \
            'такие операции: "{}"'. \
            format(', '.join(builtin_operations.keys()))
    first_arg, operation, second_arg = expr_parced
    try:
        first_arg = int(first_arg)
        second_arg = int(second_arg)
    except ValueError:
        return 'Я умею работать только с целыми числами :('
    if second_arg == 0 and operation == '/':
        return 'Еще в школе учили, на ноль делить нельзя!'
    operation = builtin_operations.get(operation)
    return '{}'.format(operation(first_arg, second_arg))


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
    dp.add_handler(CommandHandler("planet", find_planet, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", count_words, pass_args=True))
    dp.add_handler(CommandHandler("calc", calculate, pass_args=True))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)

    print('Poller has been started, now polling till the end of time...')
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
