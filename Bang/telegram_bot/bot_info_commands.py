from django.conf import settings

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext

from main.models import Bar, Party, School, Menu

from .db_usage import get_user_data_from_update, register_user_to_party
from .custom_logging import custom_info_logging, custom_warning_logging
from .QRGenerator import qr_code_image

buttons = [["Школа", "Вечеринки"],
           ["Бар", "Меню"],
           ["Зарегистрировать на вечеринку"]]

reply_markup = ReplyKeyboardMarkup(keyboard=buttons,
                                   one_time_keyboard=True,
                                   resize_keyboard=True
                                   )

FIRST_NAME_REG, LAST_NAME_REG, NUMBER_REG, END = range(4)

user_party_info = []


def start(update: Update, _: CallbackContext):
    """Send a message when a user starts a bot."""
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
        return bar(update=update, _=CallbackContext)
    elif text == "Меню":
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


def menu(update: Update, _: CallbackContext):
    """ Sends text information about menu """
    custom_info_logging(update=update, action="menu")

    text = db_commands(Menu)

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


def first_name_reg(update: Update, _: CallbackContext):
    """ Asks for first name"""
    custom_info_logging(update=update, action="first_name_reg")

    update.message.reply_text(
        text="Введите ваше имя или нажмите на /cancel для отмены",
        reply_markup=ReplyKeyboardRemove()

    )

    return LAST_NAME_REG


def last_name_reg(update: Update, _: CallbackContext):
    """ Asks for first name"""
    custom_info_logging(update=update, action="last_name_reg")

    user_party_info.append(update.message.text)

    update.message.reply_text(
        text="Введите вашу фамилию или нажмите на /cancel для отмены"
    )

    return NUMBER_REG


def number_reg(update: Update, _: CallbackContext):
    """ Asks for first name"""
    custom_info_logging(update=update, action="number_reg")

    user_party_info.append(update.message.text)

    update.message.reply_text(
        text="Введите ваш номер или нажмите на /cancel для отмены"
    )

    return END


def end(update: Update, _: CallbackContext):
    """ Ends the registration"""
    custom_info_logging(update=update, action="end")

    user_party_info.append(update.message.text)

    register_user_to_party(user_party_info, update)

    user_party_info.clear()

    qr_code = qr_code_image(update)

    update.message.bot.send_photo(chat_id=update.effective_chat.id, photo=qr_code)
    update.message.reply_text(
        text="Вы зарегестрированы",
        reply_markup=reply_markup,
    )

    return ConversationHandler.END


def cancel(update: Update, _: CallbackContext):
    """ Cancel the registration"""
    custom_info_logging(update=update, action="cancel")
    update.message.reply_text(
        text='В след раз зарегестрируетесь.',
        reply_markup=reply_markup,
    )

    return ConversationHandler.END


def error(update: Update, _: CallbackContext):
    """Log Errors caused by Updates."""
    custom_warning_logging(update=update, _=CallbackContext)
