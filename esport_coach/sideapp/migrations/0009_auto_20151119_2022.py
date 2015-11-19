# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0008_auto_20151119_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='pricerate',
            field=models.PositiveIntegerField(),
        ),
    ]
