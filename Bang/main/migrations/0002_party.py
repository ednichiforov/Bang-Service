# Generated by Django 3.2 on 2021-05-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Party",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Описание")),
                ("picture", models.ImageField(blank=True, null=True, upload_to="")),
            ],
            options={
                "verbose_name": "Вечерухи",
                "verbose_name_plural": "Вечерухи",
                "db_table": "Main_Party",
            },
        ),
    ]