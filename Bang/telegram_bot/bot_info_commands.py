from django.conf import settings
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

from main.models import Bar, Party, School
from .db_usage import get_user_data_from_update
from .custom_logging import custom_warning_logging


BUTTONS = [["DJ SCHOOL", "Вечеринки"], ["Барное меню", "Попасть в списки"]]

REPLY_MARKUP = ReplyKeyboardMarkup(
    keyboard=BUTTONS, one_time_keyboard=True, resize_keyboard=True
)

ADMINS = [628061591, 247922134]


@get_user_data_from_update
def start(update: Update, _: CallbackContext) -> None:
    """Sends a message when a user starts a bot."""

    update.message.reply_text(
        text="Привет! Нажми на кнопку.",
        reply_markup=REPLY_MARKUP,
    )


def unknown_command(update: Update, _: CallbackContext) -> None:
    """Sends a message when a user types anything unknown. """

    update.message.reply_text(
        text="Не понял тебя, нажми на кнопку ниже",
        reply_markup=REPLY_MARKUP,
    )


def commands(update: Update, _: CallbackContext):
    """ Analyzes users text massage """

    text = update.message.text

    if text == "DJ SCHOOL":
        return school(update=update, _=CallbackContext)
    elif text == "Барное меню":
        return bar(update=update, _=CallbackContext)
    elif text == "Вечеринки":
        return party(update=update, _=CallbackContext)


def db_table(Table) -> str:
    """ Takes text information from DB Table """

    text = str(Table.objects.only("text").last())

    return text


def school(update: Update, _: CallbackContext) -> None:
    """ Sends text information about school """

    text = db_table(School)

    update.message.reply_text(text=text, reply_markup=REPLY_MARKUP)


def bar(update: Update, _: CallbackContext) -> None:
    """ Sends text information about bar """

    text = db_table(Bar)

    update.message.reply_text(text=text, reply_markup=REPLY_MARKUP)


def party(update: Update, _: CallbackContext) -> None:
    """ Sends text and image information about parties """

    text = db_table(Party)

    image_name = getattr(Party.objects.last(), "picture")
    image = settings.MEDIA_URL + str(image_name)

    update.message.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=image,
    )
    update.message.reply_text(text=text, reply_markup=REPLY_MARKUP)


@custom_warning_logging
def error(update: Update, _: CallbackContext) -> None:
    """Log Errors caused by Updates."""
