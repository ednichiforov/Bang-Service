from django.test import TestCase
from datetime import datetime
from telegram_bot.models import (
    UsersStartedConv,
    PartyUsersForNearestParty,
    AllPartyUsers,
)


class TestModels(TestCase):
    def setUp(self) -> None:
        self.users_started_conv_1 = UsersStartedConv.objects.create(
            user_id=111111,
            first_name="test",
            last_name="test",
            username="test",
            is_bot=False,
        )
        self.users_started_conv_2 = UsersStartedConv.objects.create(
            user_id=222222,
            first_name="test",
            last_name="test",
            username=None,
            is_bot=False,
        )
        self.party_users_for_nearest_party_1 = PartyUsersForNearestParty.objects.create(
            user=UsersStartedConv.objects.get(user_id=111111),
            real_name="test",
            real_last_name="test",
            number="11111",
        )
        self.party_users_for_nearest_party_2 = PartyUsersForNearestParty.objects.create(
            user=UsersStartedConv.objects.get(user_id=222222),
            real_name="test",
            real_last_name="test",
            number="11111",
        )
        self.all_party_users_1 = AllPartyUsers.objects.create(
            user=UsersStartedConv.objects.get(user_id=111111),
            real_name="test",
            real_last_name="test",
            number="11111",
        )
        self.all_party_users_2 = AllPartyUsers.objects.create(
            user=UsersStartedConv.objects.get(user_id=222222),
            real_name="test",
            real_last_name="test",
            number="11111",
        )

    def test_add_information_to_DB(self):
        self.assertEquals(
            UsersStartedConv.objects.all().first(), self.users_started_conv_1
        )
        self.assertEquals(
            UsersStartedConv.objects.all().last(), self.users_started_conv_2
        )
        self.assertEquals(
            PartyUsersForNearestParty.objects.all().first(),
            self.party_users_for_nearest_party_1,
        )
        self.assertEquals(
            PartyUsersForNearestParty.objects.all().last(),
            self.party_users_for_nearest_party_2,
        )
        self.assertEquals(AllPartyUsers.objects.all().first(), self.all_party_users_1)
        self.assertEquals(AllPartyUsers.objects.all().last(), self.all_party_users_2)

    def test_models_str(self):
        self.assertEqual(str(self.users_started_conv_1), "@test")
        self.assertEqual(str(self.users_started_conv_2), "222222")
        time_now = datetime.now().strftime("%H:%M, %d %b %Y")
        self.assertEqual(
            str(self.party_users_for_nearest_party_1),
            f"Id: @test, test, зарегистрировался ({time_now})",
        )
        self.assertEqual(
            str(self.party_users_for_nearest_party_2),
            f"Id: 222222, test, зарегистрировался ({time_now})",
        )
        self.assertEqual(
            str(self.all_party_users_1),
            f"Id: @test, test, зарегистрировался ({time_now})",
        )
        self.assertEqual(
            str(self.all_party_users_2),
            f"Id: 222222, test, зарегистрировался ({time_now})",
        )
