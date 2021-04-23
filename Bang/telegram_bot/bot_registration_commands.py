from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext


from .bot_info_commands import reply_markup
from .custom_logging import custom_info_logging
from .qr_code_generator import qr_code_image
from .db_usage import register_user_to_party


FIRST_NAME_REG, LAST_NAME_REG, NUMBER_REG, END = range(4)

user_party_info = []


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
