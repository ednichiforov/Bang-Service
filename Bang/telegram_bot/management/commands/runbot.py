from django.core.management.base import BaseCommand


from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from .bot_body import start, commands, error


class Command(BaseCommand):

    def handle(self, *args, **options):
        updater = Updater(token="1731613284:AAFb38FNilx8DyedftJFnsgiiOywHLeTMBY",
                          use_context=True)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))

        dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=commands))

        # log all errors
        dispatcher.add_error_handler(error)

        updater.start_polling()

        updater.idle()
