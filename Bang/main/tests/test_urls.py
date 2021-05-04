from django.test import TestCase
from django.urls import resolve, reverse
from main.views import general, users
from telegram_bot.models import PartyUsersForNearestParty, UsersStartedConv


class TestUrls(TestCase):
    def setUp(self) -> None:
        self.user1 = UsersStartedConv.objects.create(
            user_id=1111111,
            is_bot=False,
        )
        self.user_for_nearest_party1 = PartyUsersForNearestParty.objects.create(
            user=UsersStartedConv.objects.get(user_id=1111111),
        )
        self.user2 = UsersStartedConv.objects.create(
            user_id=22,
            is_bot=True,
        )
        self.user_for_nearest_party2 = PartyUsersForNearestParty.objects.create(
            user=UsersStartedConv.objects.get(user_id=22),
        )
        self.url_general = reverse("general")
        self.url_users = reverse("users", args=["1111111"])
        self.not_url_users1 = reverse("users", args=["222"])
        self.not_url_users2 = reverse("users", args=["23"])

    def test_urls_general(self):
        self.assertEquals(resolve(self.url_general).func, general)

    def test_urls_users(self):
        self.assertEquals(resolve(self.url_users).func, users)
        self.assertNotEquals(resolve(self.not_url_users1), users)
        self.assertNotEquals(resolve(self.not_url_users2), users)
