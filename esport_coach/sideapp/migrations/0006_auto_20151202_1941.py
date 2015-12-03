# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0005_auto_20151202_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='communication_stars',
            field=models.PositiveIntegerField(null=True),
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
