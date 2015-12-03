# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0003_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='hour_rate',
            new_name='hourly_rate',
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='num_stars',
            new_name='communication_stars',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='skypename',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='rating',
        ),
        migrations.AddField(
            model_name='ratings',
            name='helpfulness_stars',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ratings',
            name='skill_stars',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
