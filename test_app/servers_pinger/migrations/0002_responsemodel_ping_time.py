# Generated by Django 4.2.6 on 2023-10-21 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers_pinger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='responsemodel',
            name='ping_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 21, 19, 40, 47, 972100, tzinfo=datetime.timezone.utc)),
        ),
    ]
