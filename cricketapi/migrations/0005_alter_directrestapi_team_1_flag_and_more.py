# Generated by Django 4.2 on 2023-07-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketapi', '0004_directrestapi_batsman_name_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directrestapi',
            name='team_1_flag',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='directrestapi',
            name='team_2_flag',
            field=models.URLField(null=True),
        ),
    ]
