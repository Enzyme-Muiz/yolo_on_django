# Generated by Django 3.1.3 on 2021-06-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_player', '0006_api_sample_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_sample',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
