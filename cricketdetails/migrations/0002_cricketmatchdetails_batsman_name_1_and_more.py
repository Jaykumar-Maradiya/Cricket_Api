# Generated by Django 4.2 on 2023-07-25 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cricketdata', '0002_matchrestapidata_slug'),
        ('cricketdetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='batsman_name_1',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='batsman_name_2',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='batting_head',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='bowler_names',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='bowling_head',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='last_30th_balls',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='match_about',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='match_rest_api_data',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='match_details', to='cricketdata.matchrestapidata'),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='reviews',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='team_1_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='team_1_score',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='team_2_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cricketmatchdetails',
            name='team_2_score',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
