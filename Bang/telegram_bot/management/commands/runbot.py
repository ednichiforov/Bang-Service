from django.core.management.base import BaseCommand

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from telegram_bot.bot_info_commands import *
from telegram_bot.bot_registration_commands import *


FIRST_NAME_REG, LAST_NAME_REG, NUMBER_REG, END = range(4)


class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(token="1731613284:AAFb38FNilx8DyedftJFnsgiiOywHLeTMBY",
                          use_context=True)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler(command="start",
                                              callback=start))

        dispatcher.add_handler(CommandHandler(command="cancel",
                                              callback=cancel))

        dispatcher.add_handler(MessageHandler(filters=Filters.regex('^(Школа|Вечеринки|Бар)$'),
                                              callback=commands))

        conv_handler = ConversationHandler(
            entry_points=[
                MessageHandler(filters=Filters.regex('^(Зарегистрировать на вечеринку)$'),
                               callback=first_name_reg),
                CommandHandler(command='cancel',
                               callback=cancel)],
            states={
                FIRST_NAME_REG: [
                    MessageHandler(filters=Filters.text,
                                   callback=first_name_reg),
                    CommandHandler(command='cancel',
                                   callback=cancel)
                ],
                LAST_NAME_REG: [
                    MessageHandler(filters=Filters.text,
                                   callback=last_name_reg),
                    CommandHandler(command='cancel',
                                   callback=cancel)
                ],
                NUMBER_REG: [
                    MessageHandler(filters=Filters.text,
                                   callback=number_reg),
                    CommandHandler(command='cancel',
                                   callback=cancel),
                ],
                END: [
                    MessageHandler(filters=Filters.text,
                                   callback=end)
                ]
            },
            fallbacks=[CommandHandler(command='cancel',
                                      callback=cancel)],
        )

        dispatcher.add_handler(conv_handler)

        dispatcher.add_error_handler(error)

        updater.start_polling()

        updater.idle()
