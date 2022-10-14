# Generated by Django 4.1.2 on 2022-10-14 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opentripmap', '0003_remove_places_dist_remove_places_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='html',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='kinds',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='osm',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='wikidata',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
