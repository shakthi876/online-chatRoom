# Generated by Django 4.0.1 on 2022-02-05 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_message_date_message_d'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='d',
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2022, 2, 5, 13, 47, 58, 164982, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
