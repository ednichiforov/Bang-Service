from django.conf import settings

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ConversationHandler, CallbackContext

from main.models import Bar, Party, School

from .db_usage import get_user_data_from_update
from .custom_logging import custom_info_logging, custom_warning_logging


buttons = [
    ["DJ SCHOOL", "Вечеринки"],
    ["Барное меню", "Попасть в списки"]
]

reply_markup = ReplyKeyboardMarkup(keyboard=buttons,
                                   one_time_keyboard=True,
                                   resize_keyboard=True
                                   )


def start(update: Update, _: CallbackContext):
    """Sends a message when a user starts a bot."""
    get_user_data_from_update(update)

    custom_info_logging(update=update, action="start")

    update.message.reply_text(
        text='Привет! Нажми на кнопку.',
        reply_markup=reply_markup,
    )


def commands(update: Update, _: CallbackContext):
    text = update.message.text
    if text == "Школа":
        return school(update=update, _=CallbackContext)
    elif text == "Бар":
        return menu(update=update, _=CallbackContext)
    elif text == "Вечеринки":
        return party(update=update, _=CallbackContext)


def db_commands(Table):
    text = str(Table.objects.only("text").last())
    return text


def school(update: Update, _: CallbackContext):
    """ Sends text information about school """
    custom_info_logging(update=update, action="school")

    text = db_commands(School)

    update.message.reply_text(
        text=text,
        reply_markup=reply_markup
    )

    return ConversationHandler.END


def bar(update: Update, _: CallbackContext):
    """ Sends text information about bar """
    custom_info_logging(update=update, action="bar")

    text = db_commands(Bar)

    update.message.reply_text(
        text=text,
        reply_markup=reply_markup
    )

    return ConversationHandler.END


def party(update: Update, _: CallbackContext):
    """ Sends text and image information about parties """
    custom_info_logging(update=update, action="party")

    text = db_commands(Party)

    image_value = getattr(Party.objects.last(), "picture")
    image = settings.MEDIA_ROOT + str(image_value)

    update.message.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image, "rb"))
    update.message.reply_text(
        text=text,
        reply_markup=reply_markup
    )

    return ConversationHandler.END


def error(update: Update, _: CallbackContext):
    """Log Errors caused by Updates."""
    custom_warning_logging(update=update, _=CallbackContext)
