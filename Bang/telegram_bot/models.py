from django.db import models


class UsersStartedConv(models.Model):
    user_id = models.IntegerField(primary_key=True, unique=True, verbose_name="Телеграм id")
    first_name = models.CharField(max_length=30, null=True, verbose_name="Имя")
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Фамилия")
    username = models.CharField(max_length=30, null=True, blank=True, verbose_name="Никнеим")
    is_bot = models.BooleanField(verbose_name="Бот")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Зарегистрирован")

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    class Meta:
        db_table = "Telegram_Reg_users"
        verbose_name = "Все пользователи"
        verbose_name_plural = "Все пользователи"


class UserActionLog(models.Model):
    user = models.ForeignKey(UsersStartedConv, on_delete=models.CASCADE)
    action = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user: {self.user}, made: {self.action}, created at {self.created_at.strftime('(%H:%M, %d %B %Y)')}"
