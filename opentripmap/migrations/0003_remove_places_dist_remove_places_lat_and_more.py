# Generated by Django 4.1.2 on 2022-10-14 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opentripmap', '0002_alter_places_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='dist',
        ),
        migrations.RemoveField(
            model_name='places',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='places',
            name='lon',
        ),
    ]