# Generated by Django 2.0.2 on 2018-05-14 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_auto_20180514_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='slug',
        ),
    ]
