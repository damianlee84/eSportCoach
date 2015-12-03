# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0006_auto_20151202_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='num_stars',
        ),
    ]
