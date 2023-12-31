# Generated by Django 4.2 on 2023-07-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('details', models.CharField(max_length=200, null=True)),
                ('team_1_flag', models.CharField(max_length=200, null=True)),
                ('team_2_flag', models.CharField(max_length=200, null=True)),
                ('match_link', models.CharField(max_length=250, null=True)),
                ('team_1_title', models.CharField(max_length=50, null=True)),
                ('team_2_title', models.CharField(max_length=50, null=True)),
                ('team_1_run', models.CharField(max_length=100, null=True)),
                ('team_2_run', models.CharField(max_length=100, null=True)),
                ('result', models.CharField(max_length=200, null=True)),
                ('schedule', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
