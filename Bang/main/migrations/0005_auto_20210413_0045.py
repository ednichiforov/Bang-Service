# Generated by Django 3.2 on 2021-04-13 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210413_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='telegram_id',
            field=models.IntegerField(),
        ),
    ]
