from django.db import models


class UsersStartedConv(models.Model):
    user_id = models.IntegerField(primary_key=True, verbose_name="Телеграм id")
    first_name = models.CharField(max_length=30, null=True, verbose_name="Имя в ТГ")
    last_name = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Фамилия в ТГ"
    )
    username = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="Никнеим в ТГ"
    )
    is_bot = models.BooleanField(verbose_name="Бот")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Зарегистрирован в Боте"
    )

    def __str__(self):
        return f"@{self.username}" if self.username is not None else f"{self.user_id}"

    class Meta:
        db_table = "Telegram_All_Users"
        verbose_name = "Пользователя"
        verbose_name_plural = "пользователи"


class PartyUsersForNearestParty(models.Model):
    user = models.OneToOneField(
        UsersStartedConv, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    real_name = models.CharField(
        max_length=30, blank=True, verbose_name="Имя для вечеринки"
    )
    real_last_name = models.CharField(
        max_length=30, blank=True, verbose_name="Фамилия для вечеринки"
    )
    number = models.CharField(
        max_length=30, blank=True, verbose_name="Номер для вечеринки"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Зарегестрировался"
    )

    def __str__(self):
        return f"Id: {self.user}, {self.real_name}, зарегистрировался {self.created_at.strftime('(%H:%M, %d %B %Y)')}"

    class Meta:
        db_table = "Telegram_Party_Users_For_Nearest_Party"
        verbose_name = "Пользователя текущей вечеринки"
        verbose_name_plural = "Пользователи текущей вечеринки"


class AllPartyUsers(models.Model):
    user = models.ForeignKey(
        UsersStartedConv, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    real_name = models.CharField(
        max_length=30, null=False, verbose_name="Имя для вечеринки"
    )
    real_last_name = models.CharField(
        max_length=30, null=False, verbose_name="Фамилия для вечеринки"
    )
    number = models.CharField(
        max_length=30, null=False, verbose_name="Номер для вечеринки"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Id: {self.user}, {self.real_name}, зарегистрировался {self.created_at.strftime('(%H:%M, %d %B %Y)')}"

    class Meta:
        db_table = "Telegram_All_Party_Users"
        verbose_name = "Пользователя всех вечеринок"
        verbose_name_plural = "Пользователи всех вечеринок"
