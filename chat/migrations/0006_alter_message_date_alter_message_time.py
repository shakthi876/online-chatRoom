# Generated by Django 4.0.1 on 2022-02-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_message_time_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.CharField(default='05-02-2022', max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.CharField(default='19:56:14', max_length=10),
        ),
    ]
