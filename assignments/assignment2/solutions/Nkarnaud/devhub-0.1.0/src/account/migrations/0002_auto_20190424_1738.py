# Generated by Django 2.1.7 on 2019-04-24 17:38

import account.models
import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('object', account.models.AccountManager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
