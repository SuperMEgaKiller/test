# Generated by Django 2.0.2 on 2018-05-10 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_restaurant_time_update'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='Restaurants',
        ),
    ]
