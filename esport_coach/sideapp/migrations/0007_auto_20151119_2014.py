# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0006_tutee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='MMR',
            field=models.IntegerField(default=0),
        ),
    ]
