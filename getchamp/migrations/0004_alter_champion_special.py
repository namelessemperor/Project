# Generated by Django 4.0.2 on 2022-03-26 15:05

import _queue
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getchamp', '0003_champion_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='Special',
            field=models.CharField(blank=True, default=_queue.Empty, max_length=100, null=True),
        ),
    ]
