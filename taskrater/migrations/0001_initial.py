# Generated by Django 4.1.2 on 2022-11-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RateData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=60, null=True)),
                ('query', models.CharField(max_length=100)),
                ('rate', models.SmallIntegerField()),
                ('job_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
