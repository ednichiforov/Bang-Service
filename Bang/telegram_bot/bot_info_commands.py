from django.conf import settings
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

from main.models import Bar, Party, School
from .db_usage import get_user_data_from_update
from .custom_logging import custom_info_logging, custom_warning_logging


BUTTONS = [["DJ SCHOOL", "Вечеринки"], ["Барное меню", "Попасть в списки"]]

REPLY_MARKUP = ReplyKeyboardMarkup(
    keyboard=BUTTONS, one_time_keyboard=True, resize_keyboard=True
)

ADMINS = [628061591, 247922134]


@custom_info_logging
def start(update: Update, _: CallbackContext) -> None:
    """Sends a message when a user starts a bot."""

    get_user_data_from_update(update)

    update.message.reply_text(
        text="Привет! Нажми на кнопку.",
        reply_markup=REPLY_MARKUP,
    )


@custom_info_logging
def unknown_command(update: Update, _: CallbackContext) -> None:
    """Sends a message when a user starts a bot."""

    get_user_data_from_update(update)

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


def db_commands(Table) -> str:
    """ Takes text information from DB Table """

    text = str(Table.objects.only("text").last())

    return text


@custom_info_logging
def school(update: Update, _: CallbackContext) -> None:
    """ Sends text information about school """

    text = db_commands(School)

    print(update)

    update.message.reply_text(text=text, reply_markup=REPLY_MARKUP)


@custom_info_logging
def bar(update: Update, _: CallbackContext) -> None:
    """ Sends text information about bar """

    text = db_commands(Bar)

    update.message.reply_text(text=text, reply_markup=REPLY_MARKUP)


@custom_info_logging
def party(update: Update, _: CallbackContext) -> None:
    """ Sends text and image information about parties """

    text = db_commands(Party)

    image_value = getattr(Party.objects.last(), "picture")
    image = settings.MEDIA_ROOT + str(image_value)

    update.message.bot.send_photo(
        chat_id=update.effective_chat.id, photo=open(image, "rb")
    )
    update.message.reply_text(text=text, reply_markup=REPLY_MARKUP)


@custom_warning_logging
def error(update: Update, _: CallbackContext) -> None:
    """Log Errors caused by Updates."""
