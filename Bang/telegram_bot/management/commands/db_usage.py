from telegram_bot.models import UsersStartedConv, UserActionLog
from django.db import IntegrityError


def get_user_data_from_update(update):
    """ Adds information about user in DB """
    user = update.message.from_user
    try:
        UsersStartedConv.objects.create(
            user_id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            is_bot=user.is_bot,
        )
    except IntegrityError:
        pass


def write_user_logs(update, action):
    user = update.message.from_user
    UserActionLog.objects.create(
            id=None,
            action=action,
            user=user.id,
        )