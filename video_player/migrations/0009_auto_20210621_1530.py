# Generated by Django 3.1.3 on 2021-06-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_player', '0008_auto_20210621_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_sample',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
