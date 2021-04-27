from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext


from .bot_info_commands import REPLY_MARKUP
from .custom_logging import custom_info_logging
from .qr_code_generator import qr_code_image
from .db_usage import register_user_to_party


FIRST_NAME_REG, LAST_NAME_REG, NUMBER_REG, USER_REGISTER_END = range(4)


user_party_info = []


@custom_info_logging
def first_name_reg(update: Update, _: CallbackContext) -> int:
    """ Asks for first name"""

    update.message.reply_text(
        text="Введите ваше имя или нажмите на /user_cancel для отмены",
        reply_markup=ReplyKeyboardRemove(),
    )

    return LAST_NAME_REG


@custom_info_logging
def last_name_reg(update: Update, _: CallbackContext) -> int:
    """ Asks for first name"""

    user_party_info.append(update.message.text)

    update.message.reply_text(
        text="Введите вашу фамилию или нажмите на /user_cancel для отмены",
    )

    return NUMBER_REG


@custom_info_logging
def number_reg(update: Update, _: CallbackContext) -> int:
    """ Asks for first name"""

    user_party_info.append(update.message.text)

    update.message.reply_text(
        text="Введите ваш номер или нажмите на /user_cancel для отмены"
    )

    return USER_REGISTER_END


@custom_info_logging
def registration_end(update: Update, _: CallbackContext) -> int:
    """ Ends the registration"""

    user_party_info.append(update.message.text)

    register_user_to_party(user_party_info, update)

    user_party_info.clear()

    qr_code = qr_code_image(update)

    update.message.bot.send_photo(chat_id=update.effective_chat.id, photo=qr_code)
    update.message.reply_text(
        text="Вы зарегестрированы",
        reply_markup=REPLY_MARKUP,
    )

    return ConversationHandler.END


@custom_info_logging
def user_cancel(update: Update, _: CallbackContext) -> int:
    """ Cancel the registration"""

    user_party_info.clear()

    update.message.reply_text(
        text="В след раз зарегестрируетесь.",
        reply_markup=REPLY_MARKUP,
    )

    return ConversationHandler.END
