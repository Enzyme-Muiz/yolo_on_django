# Generated by Django 3.1.3 on 2021-06-21 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video_player', '0005_auto_20210621_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_sample',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]