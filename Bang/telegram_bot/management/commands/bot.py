import logging

from django.core.management.base import BaseCommand
from main.models import Bar, Party, School, Menu

from telegram import Bot, ReplyKeyboardMarkup, Update
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CallbackContext
from telegram.utils.request import Request

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "1731613284:AAFb38FNilx8DyedftJFnsgiiOywHLeTMBY"

buttons = [["Школа", "Вечеринки"],
           ["Бар", "Меню"]]


def school(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    text = str(School.objects.all().last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def bar(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    text = str(Bar.objects.all().last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def menu(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    text = str(Menu.objects.all().last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def party(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    text = str(Party.objects.only("text").last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def start(update: Update, _: CallbackContext) -> int:
    text = update.message.text
    if text == "Школа":
        return school(update=update, _=CallbackContext)
    elif text == "Бар":
        return bar(update=update, _=CallbackContext)
    elif text == "Меню":
        return menu(update=update, _=CallbackContext)
    elif text == "Вечеринки":
        return party(update=update, _=CallbackContext)

    reply_markup = ReplyKeyboardMarkup(keyboard=buttons,
                                       one_time_keyboard=False,
                                       resize_keyboard=True
                                       )
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        text='Привет!',
        reply_markup=reply_markup,
    )


class Command(BaseCommand):

    def handle(self, *args, **options):

        updater = Updater(
            token=TOKEN,
            use_context=True
        )

        updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=start))

        updater.start_polling()
        updater.idle()
