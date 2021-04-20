import logging

from django.core.management.base import BaseCommand
from main.models import Bar, Party, School, Menu
from django.conf import settings
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CallbackContext, CommandHandler
from telegram.utils.request import Request
from .db_usage import get_user_data_from_update
from .decors import logging_funct

logging_funct.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging_funct.INFO
)

logger = logging_funct.getLogger(__name__)

TOKEN = "1731613284:AAFb38FNilx8DyedftJFnsgiiOywHLeTMBY"

SCHOOL, PARTY, BAR, MENU, FIRST_NAME, LAST_NAME, NUMBER = range(7)

buttons = [["Школа", "Вечеринки"],
           ["Бар", "Меню"],
           ["Зарегистрировать на вечеринку"]]


def school(update: Update, _: CallbackContext):
    """ Sends text information about school """
    user = update.message.from_user
    logger.info(f"{user.first_name}:{user.username} pressed {school.__name__} button.")
    text = str(School.objects.only("text").last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def bar(update: Update, _: CallbackContext):
    """ Sends text information about bar """
    user = update.message.from_user
    logger.info(f"{user.first_name}:{user.username} pressed bar button.")
    text = str(Bar.objects.all().last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def menu(update: Update, _: CallbackContext):
    """ Sends text information about menu """
    user = update.message.from_user
    logger.info(f"{user.first_name}:{user.username} pressed menu button.")
    text = str(Menu.objects.all().last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def party(update: Update, _: CallbackContext):
    """ Sends text and image information about parties """
    user = update.message.from_user
    logger.info(f"{user.first_name}:{user.username} pressed party button.")
    text = str(Party.objects.only("text").last())
    image_value = getattr(Party.objects.last(), "picture")
    image = settings.MEDIA_ROOT + str(image_value)
    update.message.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image, "rb"))
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def f_name_party_reg(update: Update, _: CallbackContext):
    user = update.message.from_user
    logger.info(f"{user.first_name}:{user.username} pressed menu button.")
    update.message.reply_text(
        text="Введите имя, фамилию и номер телефона, либо отмените",
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def cancel(update: Update, _: CallbackContext):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
       text='В след раз.'
    )

    return ConversationHandler.END


def commands(update: Update, _: CallbackContext):

    text = update.message.text
    if text == "Школа":
        return school(update=update, _=CallbackContext)
    elif text == "Бар":
        return bar(update=update, _=CallbackContext)
    elif text == "Меню":
        return menu(update=update, _=CallbackContext)
    elif text == "Вечеринки":
        return party(update=update, _=CallbackContext)
    elif text == "Зарегистрировать на вечеринку":
        return f_name_party_reg(update=update, _=CallbackContext)

    reply_markup = ReplyKeyboardMarkup(keyboard=buttons,
                                       one_time_keyboard=False,
                                       resize_keyboard=True
                                       )

    update.message.reply_text(
        text=' Хэй авадлаоыдап!',
        reply_markup=reply_markup,
    )




def command_start(update: Update, _: CallbackContext):
    """ Started the conversation """

    get_user_data_from_update(update)

    reply_markup = ReplyKeyboardMarkup(keyboard=buttons,
                                       one_time_keyboard=False,
                                       resize_keyboard=True
                                       )
    user = update.message.from_user
    logger.info(f"{user.first_name}:{user.username} started the conversation ")
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

        updater.dispatcher.add_handler(MessageHandler(command_start, filters=Filters.all, callback=commands))

        updater.start_polling()
        updater.idle()
