# Generated by Django 5.2 on 2025-07-11 16:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studysession',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
