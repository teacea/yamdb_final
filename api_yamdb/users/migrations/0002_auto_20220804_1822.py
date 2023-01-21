# Generated by Django 2.2.16 on 2022-08-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Авторизированный пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', max_length=15, verbose_name='Пользовательские роли'),
        ),
    ]