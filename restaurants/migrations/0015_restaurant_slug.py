# Generated by Django 2.0.2 on 2018-05-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0014_remove_restaurant_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]