from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext
from .bot_info_commands import REPLY_MARKUP
from .qr_code_generator import qr_code_image
from .db_usage import register_user_to_party


FIRST_NAME_REG, LAST_NAME_REG, NUMBER_REG, USER_REGISTER_END = range(4)


def first_name_reg(update: Update, _: CallbackContext) -> int:
    """ Asks for first name"""

    update.message.reply_text(
        text="Введите ваше имя или нажмите на /user_cancel для отмены",
        reply_markup=ReplyKeyboardRemove(),
    )

    return LAST_NAME_REG


def last_name_reg(update: Update, _: CallbackContext) -> int:
    """ Asks for first name"""

    register_user_to_party(update=update, real_name=update.message.text)

    update.message.reply_text(
        text="Введите вашу фамилию или нажмите на /user_cancel для отмены",
    )

    return NUMBER_REG


def number_reg(update: Update, _: CallbackContext) -> int:
    """ Asks for first name"""

    register_user_to_party(update=update, real_last_name=update.message.text)

    update.message.reply_text(
        text="Введите ваш номер или нажмите на /user_cancel для отмены"
    )

    return USER_REGISTER_END


def registration_end(update: Update, _: CallbackContext) -> int:
    """ Ends the registration"""

    register_user_to_party(update=update, number=update.message.text)
    print("registration_end")
    qr_code = qr_code_image(update)

    update.message.bot.send_photo(chat_id=update.effective_chat.id, photo=qr_code)
    update.message.reply_text(
        text="Вы зарегестрированы",
        reply_markup=REPLY_MARKUP,
    )

    return ConversationHandler.END


def user_cancel(update: Update, _: CallbackContext) -> int:
    """ Cancel the registration"""

    update.message.reply_text(
        text="В след раз зарегестрируетесь.",
        reply_markup=REPLY_MARKUP,
    )

    return ConversationHandler.END
