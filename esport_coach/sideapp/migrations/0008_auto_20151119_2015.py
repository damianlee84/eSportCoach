# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0007_auto_20151119_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='pricerate',
            field=models.IntegerField(),
        ),
    ]
