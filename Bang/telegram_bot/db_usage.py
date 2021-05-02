from .models import UsersStartedConv, PartyUsersForNearestParty
from django.db import IntegrityError


def get_user_data_from_update(func):
    """ Adds information about user in DB """

    def inner(update, _):
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

        return func(update, _)

    return inner


def register_user_to_party(
    update, real_name=None, real_last_name=None, number=None
) -> None:
    """ Adds information about party user in DB"""

    user = update.message.from_user

    if real_name:

        try:
            PartyUsersForNearestParty.objects.create(
                real_name=real_name,
                user=UsersStartedConv.objects.get(user_id=user.id),
            )
        except IntegrityError:
            PartyUsersForNearestParty.objects.filter(
                user=UsersStartedConv.objects.get(user_id=user.id)
            ).update(real_name=real_name)
    if real_last_name:

        try:
            PartyUsersForNearestParty.objects.create(
                real_last_name=real_last_name,
                user=UsersStartedConv.objects.get(user_id=user.id),
            )
        except IntegrityError:
            PartyUsersForNearestParty.objects.filter(
                user=UsersStartedConv.objects.get(user_id=user.id)
            ).update(real_last_name=real_last_name)
    if number:

        try:
            PartyUsersForNearestParty.objects.create(
                number=number,
                user=UsersStartedConv.objects.get(user_id=user.id),
            )
        except IntegrityError:
            PartyUsersForNearestParty.objects.filter(
                user=UsersStartedConv.objects.get(user_id=user.id)
            ).update(number=number)
