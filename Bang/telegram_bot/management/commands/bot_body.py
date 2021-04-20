from django.conf import settings

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext

from main.models import Bar, Party, School, Menu

from .db_usage import get_user_data_from_update
from .custom_logging import *

buttons = [["Школа", "Вечеринки"],
           ["Бар", "Меню"],
           ["Зарегистрировать на вечеринку"]]


def start(update: Update, _: CallbackContext):
    """Send a message when a user starts a bot."""
    get_user_data_from_update(update)

    reply_markup = ReplyKeyboardMarkup(keyboard=buttons,
                                       one_time_keyboard=False,
                                       resize_keyboard=True
                                       )

    custom_logging(update=update, action="start")

    update.message.reply_text(
        text='Привет! Нажми на кнопку.',
        reply_markup=reply_markup,
    )


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

    reply_markup = ReplyKeyboardMarkup(keyboard=buttons,
                                       one_time_keyboard=True,
                                       resize_keyboard=True
                                       )
    update.message.reply_text(
        text='Нажми на кнопку',
        reply_markup=reply_markup,
    )


def school(update: Update, _: CallbackContext):
    """ Sends text information about school """
    custom_logging(update=update, action="school")

    text = str(School.objects.only("text").last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def bar(update: Update, _: CallbackContext):
    """ Sends text information about bar """
    custom_logging(update=update, action="bar")

    text = str(Bar.objects.all().last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def menu(update: Update, _: CallbackContext):
    """ Sends text information about menu """
    custom_logging(update=update, action="menu")

    text = str(Menu.objects.all().last())
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def party(update: Update, _: CallbackContext):
    """ Sends text and image information about parties """
    custom_logging(update=update, action="party")

    text = str(Party.objects.only("text").last())
    image_value = getattr(Party.objects.last(), "picture")
    image = settings.MEDIA_ROOT + str(image_value)
    update.message.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image, "rb"))
    update.message.reply_text(
        text=text
    )

    return ConversationHandler.END


def error(update: Update, _: CallbackContext):
    """Log Errors caused by Updates."""
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, _.error)
