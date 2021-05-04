from django.test import TestCase, Client
from django.urls import reverse
from telegram_bot.models import PartyUsersForNearestParty, UsersStartedConv


class TestUrls(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url_general = reverse("general")
        self.url_users = reverse("users", args=["0000"])

        self.user1 = UsersStartedConv.objects.create(
            user_id=0000,
            is_bot=False,
        )
        self.user_for_nearest_party1 = PartyUsersForNearestParty.objects.create(
            user=UsersStartedConv.objects.get(user_id=0000),
        )

    def test_views_general_GET(self):
        response_general = self.client.get(self.url_general)
        self.assertEquals(response_general.status_code, 200)
        self.assertTemplateUsed(response_general, "main/index.html")

    def test_views_users_GET(self):
        response_users = self.client.get(self.url_users)
        self.assertEquals(response_users.status_code, 200)
        self.assertTemplateUsed(response_users, "main/users.html")
