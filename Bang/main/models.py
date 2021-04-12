from django.db import models


class School(models.Model):
    name = "Школа"
    text = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Main_School"
        verbose_name = "Школа"
        verbose_name_plural = "Школа"


class Party(models.Model):
    name = "Вечерухи"
    text = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Main_Party"
        verbose_name = "Вечерухи"
        verbose_name_plural = "Вечерухи"


class Bar(models.Model):
    name = "Бар"
    text = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Main_Bar"
        verbose_name = "Бар"
        verbose_name_plural = "Бар"


class Menu(models.Model):
    name = "Меню"
    text = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Main_Menu"
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
