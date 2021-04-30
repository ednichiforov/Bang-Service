from django.db import models


class School(models.Model):
    text = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.text

    class Meta:
        db_table = "Main_School"
        verbose_name = "DJ SCHOOL"
        verbose_name_plural = "DJ SCHOOL"


class Party(models.Model):
    text = models.TextField(verbose_name="Описание")
    picture = models.ImageField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.text

    class Meta:
        db_table = "Main_Party"
        verbose_name = "Вечерухи"
        verbose_name_plural = "Вечерухи"


class Bar(models.Model):
    text = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.text

    class Meta:
        db_table = "Main_Bar"
        verbose_name = "Барное меню"
        verbose_name_plural = "Барное меню"


class About(models.Model):
    text = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.text

    class Meta:
        db_table = "Main_About"
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
