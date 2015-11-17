# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sideapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 2, 8, 1, 453988, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
