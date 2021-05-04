from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ConversationHandler, CallbackContext
from .bot_info_commands import REPLY_MARKUP
from .models import UsersStartedConv


ADMIN_CONV, LOADING_INFO = range(2)

ADMINS = [628061591, 247922134]


def admin_starts_conv(update: Update, _: CallbackContext) -> int:
    """ Asks for information"""

    user = update.message.from_user

    if user.id in ADMINS:
        update.message.reply_text(
            text="Жду от тебя инфу или нажми /admin_cancel для отмены",
            reply_markup=ReplyKeyboardRemove(),
        )
        return LOADING_INFO
    else:
        update.message.reply_text(text="Ой ты не Гаппа")
        return ConversationHandler.END


def admin_loading_info(update: Update, _: CallbackContext) -> int:
    """ Sends information to all"""

    text = update.message.text
    photo = update.message.photo
    video = update.message.video
    caption = update.message.caption

    users_id_queryset = UsersStartedConv.objects.values_list("user_id")
    users_id = [user[0] for user in users_id_queryset]
    chats_id = users_id

    for chat_id in chats_id:
        if photo and caption:
            update.message.bot.send_photo(photo=photo[0], chat_id=chat_id)
            update.message.bot.send_message(text=caption, chat_id=chat_id)
        elif video and caption:
            update.message.bot.send_video(video=video, chat_id=chat_id)
            update.message.bot.send_message(text=caption, chat_id=chat_id)
        elif text:
            update.message.bot.send_message(text=text, chat_id=chat_id)
        elif photo:
            update.message.bot.send_photo(photo=photo[0], chat_id=chat_id)
        elif video:
            update.message.bot.send_video(video=video, chat_id=chat_id)

    update.message.reply_text(
        text="Вcё отправил",
        reply_markup=REPLY_MARKUP,
    )

    return ConversationHandler.END


def admin_cancel(update: Update, _: CallbackContext) -> int:
    """ Cancel the conversation"""

    update.message.reply_text(
        text="Передумал",
        reply_markup=REPLY_MARKUP,
    )

    return ConversationHandler.END
