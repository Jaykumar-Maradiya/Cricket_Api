# Generated by Django 4.2 on 2023-07-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchrestapidata',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=True),
        ),
    ]
