from .models import UsersStartedConv, PartyUsersForNearestParty
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


def register_user_to_party(user_party_info, update):
    """ Adds information about party user in DB"""
    user = update.message.from_user
    try:
        PartyUsersForNearestParty.objects.create(
            real_name=user_party_info[0],
            real_last_name=user_party_info[1],
            number=user_party_info[2],
            user=UsersStartedConv.objects.get(user_id=user.id),
        )
    except IndexError:
        pass
