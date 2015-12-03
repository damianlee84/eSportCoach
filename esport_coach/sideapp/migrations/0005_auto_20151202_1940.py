# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0004_auto_20151202_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='hourly_rate',
            new_name='hour_rate',
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='communication_stars',
            new_name='num_stars',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='skypename',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='helpfulness_stars',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='skill_stars',
        ),
        migrations.AddField(
            model_name='coach',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
