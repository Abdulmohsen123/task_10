# Generated by Django 2.0.4 on 2018-07-19 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20180719_1143'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RestaurantItem',
            new_name='Item',
        ),
    ]
